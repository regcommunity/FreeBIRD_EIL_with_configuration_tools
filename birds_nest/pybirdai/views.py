# coding=UTF-8
# Copyright (c) 2024 Bird Software Solutions Ltd
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License 2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#    Neil Mackenzie - initial API and implementation
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django.db import transaction, connection
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.core import serializers
from .bird_meta_data_model import (
    VARIABLE_MAPPING, VARIABLE_MAPPING_ITEM, MEMBER_MAPPING, MEMBER_MAPPING_ITEM,
    CUBE_LINK, CUBE_STRUCTURE_ITEM_LINK, MAPPING_TO_CUBE, MAPPING_DEFINITION,
    COMBINATION, COMBINATION_ITEM, CUBE, CUBE_STRUCTURE_ITEM, VARIABLE, MEMBER,
    MAINTENANCE_AGENCY,  MEMBER_HIERARCHY, DOMAIN
)
import json
from . import bird_meta_data_model
from .entry_points.import_input_model import RunImportInputModelFromSQLDev

from .entry_points.import_report_templates_from_website import RunImportReportTemplatesFromWebsite
from .entry_points.import_semantic_integrations_from_website import RunImportSemanticIntegrationsFromWebsite
from .entry_points.import_hierarchy_analysis_from_website import RunImportHierarchiesFromWebsite
from .entry_points.create_filters import RunCreateFilters
from .entry_points.create_joins_metadata import RunCreateJoinsMetadata
from .entry_points.delete_joins_metadata import RunDeleteJoinsMetadata
from .entry_points.create_executable_joins import RunCreateExecutableJoins
from .entry_points.run_create_executable_filters import RunCreateExecutableFilters
from .entry_points.execute_datapoint import RunExecuteDataPoint
from .entry_points.upload_sqldev_eil_files import UploadSQLDevEILFiles
from .entry_points.upload_sqldev_eldm_files import UploadSQLDevELDMFiles
from .entry_points.upload_technical_export_files import UploadTechnicalExportFiles
from .entry_points.create_django_models import RunCreateDjangoModels
from .entry_points.convert_ldm_to_sdd_hierarchies import RunConvertLDMToSDDHierarchies
import os
import csv
from pathlib import Path
from .process_steps.upload_files.file_uploader import FileUploader
from .entry_points.delete_bird_metadata_database import RunDeleteBirdMetadataDatabase
from .entry_points.upload_joins_configuration import UploadJoinsConfiguration
from django.template.loader import render_to_string
from django.db.models import Count, F
from django.views.generic import ListView
from django.urls import reverse
from .context.sdd_context_django import SDDContext
from urllib.parse import unquote
import logging
import zipfile
from .context.csv_column_index_context import ColumnIndexes
from django.apps import apps
from django.db import models
import inspect
from .utils.mapping_library import (
    build_mapping_results,
    add_variable_to_mapping,
    create_or_update_member,
    update_member_mapping_item,
    process_related_mappings,
    process_member_mappings,
    create_table_data,
    get_reference_variables,
    cascade_member_mapping_changes,
    process_mapping_chain
)
import time
from datetime import datetime
from typing import Dict, List, Set, Tuple, Any, Optional
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Helper function for paginated modelformset views
def paginated_modelformset_view(request, model, template_name, order_by=None):
    # Get all maintenance agencies for the create form
    maintenance_agencies = MAINTENANCE_AGENCY.objects.all().order_by('name')

    # Get all member mappings and variable mappings for dropdowns
    member_mappings = MEMBER_MAPPING.objects.all().order_by('name')
    variable_mappings = VARIABLE_MAPPING.objects.all().order_by('name')

    # Get paginated formset
    page_number = request.GET.get('page', 1)
    queryset = model.objects.all()
    if order_by:
        queryset = queryset.order_by(order_by)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(model, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, f'{model.__name__} updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, f'There was an error updating the {model.__name__}.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'maintenance_agencies': maintenance_agencies,
        'member_mappings': member_mappings,
        'variable_mappings': variable_mappings,
    }
    return render(request, template_name, context)

def show_report(request, report_id):
    return render(request, 'pybirdai/' + report_id)

# Views for running various processes
def run_create_joins_meta_data(request):
    if request.GET.get('execute') == 'true':
        # Execute the actual task
        app_config = RunCreateJoinsMetadata('pybirdai', 'birds_nest')
        app_config.run_create_joins_meta_data()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Joins Metadata (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Joins Metadata created successfully.",
        '/pybirdai/create-transformation-rules-in-smcubes',
        "Create Transformations Rules MetaData"
    )

def create_django_models(request):
    if request.GET.get('execute') == 'true':
        app_config = RunCreateDjangoModels('pybirdai', 'birds_nest')
        app_config.ready()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Django Models",
        "Created Django Models successfully.",
        '/pybirdai/create-bird-database',
        "Create BIRD Database"
    )

def run_create_python_joins(request):
    if request.GET.get('execute') == 'true':
        app_config = RunCreateExecutableJoins('pybirdai', 'birds_nest')
        app_config.create_python_joins()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Python Joins (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Created Executable Joins in Python",
        '/pybirdai/create-transformation-rules-in-python',
        "Create Transformations Rules in Python"
    )



def run_delete_joins_meta_data(request):
    if request.GET.get('execute') == 'true':
        app_config = RunDeleteJoinsMetadata('pybirdai', 'birds_nest')
        app_config.run_delete_joins_meta_data()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Deleting Joins Metadata",
        "Deleted Transformation Metadata successfully",
        '/pybirdai/create-transformation-rules-in-smcubes',
        "Create Transformations Rules MetaData"
    )

def delete_existing_contents_of_bird_metadata_database(request):
    if request.GET.get('execute') == 'true':
        app_config = RunDeleteBirdMetadataDatabase('pybirdai', 'birds_nest')
        app_config.run_delete_bird_metadata_database()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Deleting Bird Metadata Database",
        "Deleted Bird Metadata Database",
        '/pybirdai/populate-bird-metadata-database',
        "Populate BIRD Metadata Database"
    )

def run_import_semantic_integrations_from_website(request):
    if request.GET.get('execute') == 'true':
        app_config = RunImportSemanticIntegrationsFromWebsite('pybirdai', 'birds_nest')
        app_config.import_mappings_from_website()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Importing Semantic Integrations (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Import Semantic Integrations completed successfully.",
        '/pybirdai/create-transformation-rules-configuration',
        "Create Transformations Rules Configuration"
    )

def run_import_input_model_from_sqldev(request):
    if request.GET.get('execute') == 'true':
        app_config = RunImportInputModelFromSQLDev('pybirdai', 'birds_nest')
        app_config.ready()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Importing Input Model from SQLDev (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Import Input Model from SQLDev process completed successfully",
        '/pybirdai/populate-bird-metadata-database',
        "Populate BIRD Metadata Database"
    )




def run_import_hierarchies(request):
    if request.GET.get('execute') == 'true':
        app_config = RunImportHierarchiesFromWebsite('pybirdai', 'birds_nest')
        app_config.import_hierarchies()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Importing Hierarchies (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Import hierarchies completed successfully.",
        '/pybirdai/create-transformation-rules-configuration',
        "Create Transformations Rules Configuration"
    )


def import_report_templates(request):
    if request.GET.get('execute') == 'true':
        app_config = RunImportReportTemplatesFromWebsite('pybirdai', 'birds_nest')
        app_config.run_import()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Importing Report Templates (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Import Report templates from website completed successfully.",
        '/pybirdai/populate-bird-metadata-database',
        "Populate BIRD Metadata Database"
    )

def run_create_filters(request):
    if request.GET.get('execute') == 'true':
        # Execute the actual task
        app_config = RunCreateFilters('pybirdai', 'birds_nest')
        app_config.run_create_filters()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Filters (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Filters created successfully.",
        '/pybirdai/create-transformation-rules-in-smcubes',
        "Create Transformations Rules MetaData"
    )


def run_create_executable_filters(request):
    if request.GET.get('execute') == 'true':
        app_config = RunCreateExecutableFilters('pybirdai', 'birds_nest')
        app_config.run_create_executable_filters()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Executable Filters (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Create executable filters process completed successfully",
        '/pybirdai/create-transformation-rules-in-python',
        "Create Transformations Rules in Python"
    )

def upload_sqldev_eil_files(request):
    if request.method == 'GET':
        # Show the upload form
        return render(request, 'pybirdai/upload_sqldev_eil_files.html')
    elif request.method == 'POST':
        # Handle the file upload

        app_config = UploadSQLDevEILFiles('pybirdai', 'birds_nest')
        app_config.upload_sqldev_eil_files(request)

        #result = app_config.upload_sqldev_eil_files()

        #if result['status'] == 'success':
        #   messages.success(request, 'Files uploaded successfully')
        #else:
        #    messages.error(request, result['message'])

        html_response = f"""
        <h3>Uploaded SQLDeveloper EILFiles.</h3>

        <p> Go back to <a href="/pybirdai/create-bird-database">Create BIRD Database</a></p>
    """
    return HttpResponse(html_response)

def upload_sqldev_eldm_files(request):
    if request.method == 'GET':
        # Show the upload form
        return render(request, 'pybirdai/upload_sqldev_eldm_files.html')
    elif request.method == 'POST':
        # Handle the file upload
        app_config = UploadSQLDevELDMFiles('pybirdai', 'birds_nest')
        app_config.upload_sqldev_eldm_files(request)
        html_response = f"""
        <h3>Uploaded SQLDeveloper ELDMFiles.</h3>

        <p> Go back to <a href="/pybirdai/create-bird-database">Create BIRD Database</a></p>
    """
    return HttpResponse(html_response)

def upload_technical_export_files(request):
    if request.method == 'GET':
        # Show the upload form
        return render(request, 'pybirdai/upload_technical_export_files.html')
    elif request.method == 'POST':
        # Handle the file upload

        app_config = UploadTechnicalExportFiles('pybirdai', 'birds_nest')
        app_config.upload_technical_export_files(request)

        #result = app_config.upload_sqldev_eil_files()

        #if result['status'] == 'success':
        #   messages.success(request, 'Files uploaded successfully')
        #else:
        #    messages.error(request, result['message'])


        html_response = f"""
            <h3>Uploaded Technical Export Files.</h3>

            <p> Go back to <a href="/pybirdai/populate-bird-metadata-database">Populate BIRD Metadata Database</a></p>
        """
        return HttpResponse(html_response)

def upload_joins_configuration(request):

    if request.method == 'GET':
        # Show the upload form
        return render(request, 'pybirdai/upload_joins_configuration.html')
    elif request.method == 'POST':
        # Handle the file upload

        app_config = UploadJoinsConfiguration('pybirdai', 'birds_nest')
        app_config.upload_joins_configuration(request)

        #result = app_config.upload_sqldev_eil_files()

        #if result['status'] == 'success':
        #   messages.success(request, 'Files uploaded successfully')
        #else:
        #    messages.error(request, result['message'])


        html_response = f"""
            <h3>Uploaded Joins Configuration Files.</h3>

            <p> Go back to <a href="/pybirdai/create-transformation-rules-configuration">Create Transformations Rules Configuration</a></p>
        """
        return HttpResponse(html_response)

# Basic views
def index(request):
    return HttpResponse("Hello, world. You're at the pybirdai index.")

def home_view(request):
    return render(request, 'pybirdai/home.html')

# CRUD views for various models
def edit_variable_mappings(request):
    # Get all maintenance agencies for the create form
    maintenance_agencies = MAINTENANCE_AGENCY.objects.all().order_by('name')

    # Get paginated formset
    page_number = request.GET.get('page', 1)
    all_items = VARIABLE_MAPPING.objects.all().order_by('variable_mapping_id')
    paginator = Paginator(all_items, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(VARIABLE_MAPPING, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, 'Variable Mappings updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error updating the Variable Mappings.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'maintenance_agencies': maintenance_agencies,
    }
    return render(request, 'pybirdai/edit_variable_mappings.html', context)

def edit_variable_mapping_items(request):
    # Get unique values for filters
    unique_variable_mappings = VARIABLE_MAPPING_ITEM.objects.values_list('variable_mapping_id', flat=True).distinct()
    unique_variables = VARIABLE_MAPPING_ITEM.objects.values_list('variable_id', flat=True).distinct()

    # Get all variable mappings and variables for the create form
    all_variable_mappings = VARIABLE_MAPPING.objects.all().order_by('variable_mapping_id')
    all_variables = VARIABLE.objects.all().order_by('variable_id')

    # Get filter values from request
    selected_variable_mapping = request.GET.get('variable_mapping_id', '')
    selected_variable = request.GET.get('variable_id', '')

    # Apply filters and ordering
    queryset = VARIABLE_MAPPING_ITEM.objects.all().order_by('id')
    if selected_variable_mapping:
        queryset = queryset.filter(variable_mapping_id=selected_variable_mapping)
    if selected_variable:
        queryset = queryset.filter(variable_id=selected_variable)

    # Add pagination and formset creation
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(VARIABLE_MAPPING_ITEM, fields='__all__', extra=0)
    formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'unique_variable_mappings': unique_variable_mappings,
        'unique_variables': unique_variables,
        'selected_variable_mapping': selected_variable_mapping,
        'selected_variable': selected_variable,
        'all_variable_mappings': all_variable_mappings,
        'all_variables': all_variables,
    }
    return render(request, 'pybirdai/edit_variable_mapping_items.html', context)

def create_variable_mapping_item(request):
    if request.method == 'POST':
        try:
            # Get form data
            variable_mapping = get_object_or_404(VARIABLE_MAPPING, variable_mapping_id=request.POST.get('variable_mapping_id'))
            variable = get_object_or_404(VARIABLE, variable_id=request.POST.get('variable_id'))

            # Create new item
            item = VARIABLE_MAPPING_ITEM(
                variable_mapping_id=variable_mapping,
                is_source=request.POST.get('is_source'),
                variable_id=variable,
                valid_from=request.POST.get('valid_from') or None,
                valid_to=request.POST.get('valid_to') or None
            )
            item.save()

            messages.success(request, 'Variable Mapping Item created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating Variable Mapping Item: {str(e)}')

    return redirect('pybirdai:edit_variable_mapping_items')

def edit_member_mappings(request):
    # Get all maintenance agencies for the create form
    maintenance_agencies = MAINTENANCE_AGENCY.objects.all().order_by('name')

    # Get paginated formset
    page_number = request.GET.get('page', 1)
    all_items = MEMBER_MAPPING.objects.all().order_by('member_mapping_id')
    paginator = Paginator(all_items, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(MEMBER_MAPPING, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, 'MEMBER_MAPPING updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error updating the MEMBER_MAPPING.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'maintenance_agencies': maintenance_agencies,
    }
    return render(request, 'pybirdai/edit_member_mappings.html', context)

def edit_member_mapping_items(request):
    # Get unique values for filters
    member_mappings = MEMBER_MAPPING_ITEM.objects.values_list('member_mapping_id', flat=True).distinct()
    members = MEMBER_MAPPING_ITEM.objects.values_list('member_id', flat=True).distinct()
    variables = MEMBER_MAPPING_ITEM.objects.values_list('variable_id', flat=True).distinct()

    # Get all available choices for dropdowns
    all_member_mappings = MEMBER_MAPPING.objects.all().order_by('member_mapping_id')
    all_members = MEMBER.objects.all().order_by('member_id')
    all_variables = VARIABLE.objects.all().order_by('variable_id')
    all_member_hierarchies = MEMBER_HIERARCHY.objects.all().order_by('member_hierarchy_id')

    # Get filter values from request
    selected_member_mapping = request.GET.get('member_mapping_id', '')
    selected_member = request.GET.get('member_id', '')
    selected_variable = request.GET.get('variable_id', '')
    selected_is_source = request.GET.get('is_source', '')

    # Apply filters
    queryset = MEMBER_MAPPING_ITEM.objects.all().order_by('id')
    if selected_member_mapping:
        queryset = queryset.filter(member_mapping_id=selected_member_mapping)
    if selected_member:
        queryset = queryset.filter(member_id=selected_member)
    if selected_variable:
        queryset = queryset.filter(variable_id=selected_variable)
    if selected_is_source:
        # Handle both lowercase and uppercase boolean strings
        if selected_is_source.lower() == 'true':
            queryset = queryset.filter(is_source__in=['true', 'True'])
        else:
            queryset = queryset.filter(is_source__in=['false', 'False'])

    # Add pagination and formset creation
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(MEMBER_MAPPING_ITEM, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, 'Member Mapping Items updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error updating the Member Mapping Items.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'member_mappings': member_mappings,
        'members': members,
        'variables': variables,
        'selected_member_mapping': selected_member_mapping,
        'selected_member': selected_member,
        'selected_variable': selected_variable,
        'selected_is_source': selected_is_source,
        'all_member_mappings': all_member_mappings,
        'all_members': all_members,
        'all_variables': all_variables,
        'all_member_hierarchies': all_member_hierarchies,
    }
    return render(request, 'pybirdai/edit_member_mapping_items.html', context)

def edit_cube_links(request):
    # Get unique values for filters
    foreign_cubes = CUBE_LINK.objects.values_list('foreign_cube_id', flat=True).distinct()
    join_identifiers = CUBE_LINK.objects.values_list('join_identifier', flat=True).distinct()

    # Get all cubes for the add form
    all_cubes = CUBE.objects.all().order_by('cube_id')

    # Get filter values from request
    selected_foreign_cube = request.GET.get('foreign_cube', '')
    selected_identifier = request.GET.get('join_identifier', '')

    # Apply filters and ordering
    queryset = CUBE_LINK.objects.all().order_by('cube_link_id')  # Add default ordering
    if selected_foreign_cube:
        queryset = queryset.filter(foreign_cube_id=selected_foreign_cube)
    if selected_identifier:
        queryset = queryset.filter(join_identifier=selected_identifier)

    # Add pagination and formset creation
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(CUBE_LINK, fields='__all__', extra=0)
    formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'foreign_cubes': foreign_cubes,
        'join_identifiers': join_identifiers,
        'selected_foreign_cube': selected_foreign_cube,
        'selected_identifier': selected_identifier,
        'all_cubes': all_cubes,
    }
    return render(request, 'pybirdai/edit_cube_links.html', context)

def edit_cube_structure_item_links(request):
    # Get unique values for dropdowns
    queryset = CUBE_STRUCTURE_ITEM_LINK.objects.all().order_by('cube_structure_item_link_id')
    unique_cube_links = CUBE_LINK.objects.values_list('cube_link_id', flat=True).distinct()

    # Get filter values from request
    selected_cube_link = request.GET.get('cube_link', '')

    # Apply filters
    if selected_cube_link:
        queryset = queryset.filter(cube_link_id=selected_cube_link)
        # Get the selected cube link object to access foreign and primary cubes
        cube_link = CUBE_LINK.objects.get(cube_link_id=selected_cube_link)
        # Get cube structure items for foreign and primary cubes
        foreign_cube_items = CUBE_STRUCTURE_ITEM.objects.filter(
            cube_structure_id=cube_link.foreign_cube_id.cube_structure_id
        ).order_by('variable_id')
        primary_cube_items = CUBE_STRUCTURE_ITEM.objects.filter(
            cube_structure_id=cube_link.primary_cube_id.cube_structure_id
        ).order_by('variable_id')
    else:
        foreign_cube_items = []
        primary_cube_items = []

    # Add pagination and formset creation
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(CUBE_STRUCTURE_ITEM_LINK, fields='__all__', extra=0)
    formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'unique_cube_links': unique_cube_links,
        'foreign_cube_items': foreign_cube_items,
        'primary_cube_items': primary_cube_items,
        'selected_cube_link': selected_cube_link,
    }

    return render(request, 'pybirdai/edit_cube_structure_item_links.html', context)

def edit_mapping_to_cubes(request):
    # Get filter parameters
    mapping_filter = request.GET.get('mapping_filter')
    cube_filter = request.GET.get('cube_filter')

    # Start with all objects and order them
    queryset = MAPPING_TO_CUBE.objects.all().order_by('mapping_id__name', 'cube_mapping_id')

    # Apply filters if they exist
    if mapping_filter:
        queryset = queryset.filter(mapping_id__mapping_id=mapping_filter)
    if cube_filter:
        queryset = queryset.filter(cube_mapping_id=cube_filter)

    # Get all mapping definitions and unique cube mappings for the dropdowns
    mapping_definitions = MAPPING_DEFINITION.objects.all().order_by('name')
    cube_mappings = (MAPPING_TO_CUBE.objects
                    .values_list('cube_mapping_id', flat=True)
                    .distinct()
                    .order_by('cube_mapping_id'))

    # Paginate after filtering
    paginator = Paginator(queryset, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Create formset for the current page
    MappingToCubeFormSet = modelformset_factory(
        MAPPING_TO_CUBE,
        fields=('mapping_id', 'cube_mapping_id', 'valid_from', 'valid_to'),
        extra=0
    )

    if request.method == 'POST':
        formset = MappingToCubeFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Changes saved successfully.')
            return redirect('pybirdai:edit_mapping_to_cubes')
    else:
        formset = MappingToCubeFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'mapping_definitions': mapping_definitions,
        'cube_mappings': cube_mappings,
    }

    return render(request, 'pybirdai/edit_mapping_to_cubes.html', context)

def edit_mapping_definitions(request):
    return paginated_modelformset_view(request, MAPPING_DEFINITION, 'pybirdai/edit_mapping_definitions.html', order_by='mapping_id')

def create_mapping_definition(request):
    if request.method == 'POST':
        try:
            maintenance_agency = None
            if request.POST.get('maintenance_agency_id'):
                maintenance_agency = get_object_or_404(MAINTENANCE_AGENCY, maintenance_agency_id=request.POST.get('maintenance_agency_id'))

            member_mapping = None
            if request.POST.get('member_mapping_id'):
                member_mapping = get_object_or_404(MEMBER_MAPPING, member_mapping_id=request.POST.get('member_mapping_id'))

            variable_mapping = None
            if request.POST.get('variable_mapping_id'):
                variable_mapping = get_object_or_404(VARIABLE_MAPPING, variable_mapping_id=request.POST.get('variable_mapping_id'))

            mapping_definition = MAPPING_DEFINITION(
                name=request.POST.get('name'),
                code=request.POST.get('code'),
                maintenance_agency_id=maintenance_agency,
                mapping_id=request.POST.get('mapping_id'),
                mapping_type=request.POST.get('mapping_type'),
                member_mapping_id=member_mapping,
                variable_mapping_id=variable_mapping
            )
            mapping_definition.save()

            messages.success(request, 'Mapping Definition created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating Mapping Definition: {str(e)}')

    return redirect('pybirdai:edit_mapping_definitions')

# Delete views for various models
def delete_item(request, model, id_field, redirect_view, decoded_id=None):
    try:
        id_value = decoded_id if decoded_id is not None else request.POST.get('id')
        if id_value is None:
            id_value = request.POST.get(id_field)
        item = get_object_or_404(model, **{id_field: id_value})
        item.delete()
        messages.success(request, f'{model.__name__} deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting {model.__name__}: {str(e)}')
    return redirect(f'pybirdai:{redirect_view}')

def delete_variable_mapping(request, variable_mapping_id):
    return delete_item(request, VARIABLE_MAPPING, 'variable_mapping_id', 'edit_variable_mappings', variable_mapping_id)

def execute_data_point(request, data_point_id):
    app_config = RunExecuteDataPoint('pybirdai', 'birds_nest')
    result = app_config.run_execute_data_point(data_point_id)

    html_response = f"""

        <h3>DataPoint Execution Results</h3>
        <p><strong>DataPoint ID:</strong> {data_point_id}</p>
        <p><strong>Result:</strong> {result}</p>
        <p><a href="/pybirdai/lineage/">View Lineage Files</a></p>
        <p><a href="/pybirdai/report-templates/">Back to the PyBIRD Reports Templates Page</a></p>
    """
    return HttpResponse(html_response)

def delete_variable_mapping_item(request):
    if request.method == 'POST':
        try:
            variable_mapping_id = request.GET.get('variable_mapping_id')
            variable_id = request.GET.get('variable_id')
            is_source = request.GET.get('is_source')

            # Get the item using the composite key
            item = get_object_or_404(
                VARIABLE_MAPPING_ITEM,
                variable_mapping_id=variable_mapping_id,
                variable_id=variable_id,
                is_source=is_source
            )

            item.delete()
            messages.success(request, 'Variable Mapping Item deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting Variable Mapping Item: {str(e)}')

    return redirect('pybirdai:edit_variable_mapping_items')

def delete_member_mapping(request, member_mapping_id):
    return delete_item(request, MEMBER_MAPPING, 'member_mapping_id', 'edit_member_mappings')

def delete_member_mapping_item(request, item_id):
    if request.method == 'POST':
        try:
            # Get the composite key fields from GET parameters
            member_mapping_id = request.GET.get('member_mapping_id')
            member_id = request.GET.get('member_id')
            variable_id = request.GET.get('variable_id')
            is_source = request.GET.get('is_source')
            member_mapping_row = request.GET.get('member_mapping_row')

            # Get the item using the composite key
            item = get_object_or_404(
                MEMBER_MAPPING_ITEM,
                member_mapping_id=member_mapping_id,
                member_id=member_id,
                variable_id=variable_id,
                is_source=is_source,
                member_mapping_row=member_mapping_row
            )

            item.delete()
            messages.success(request, 'Member Mapping Item deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting MEMBER_MAPPING_ITEM: {str(e)}')

    return redirect('pybirdai:edit_member_mapping_items')

def delete_cube_link(request, cube_link_id):
    try:
        link = get_object_or_404(CUBE_LINK, cube_link_id=cube_link_id)

        # Update the in-memory dictionaries
        sdd_context = SDDContext()

        # Remove from cube_link_dictionary
        try:
            del sdd_context.cube_link_dictionary[cube_link_id]
        except KeyError:
            pass

        # Remove from cube_link_to_foreign_cube_map
        try:
            del sdd_context.cube_link_to_foreign_cube_map[cube_link_id]
        except KeyError:
            pass

        # Remove from cube_link_to_join_identifier_map
        try:
            del sdd_context.cube_link_to_join_identifier_map[cube_link_id]
        except KeyError:
            pass

        # Remove from cube_link_to_join_for_report_id_map
        try:
            del sdd_context.cube_link_to_join_for_report_id_map[cube_link_id]
        except KeyError:
            pass

        # Delete the database record
        link.delete()
        messages.success(request, 'CUBE_LINK deleted successfully.')
        return JsonResponse({'status': 'success'})
    except Exception as e:
        messages.error(request, f'Error deleting CUBE_LINK: {str(e)}')
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

def delete_cube_structure_item_link(request, cube_structure_item_link_id):
    try:
        link = get_object_or_404(CUBE_STRUCTURE_ITEM_LINK, cube_structure_item_link_id=cube_structure_item_link_id)
        # Store the cube_link_id before deleting
        cube_link_id = link.cube_link_id.cube_link_id if link.cube_link_id else None
        link.delete()

        # Update the in-memory dictionaries
        sdd_context = SDDContext()

        # Remove from cube_structure_item_links_dictionary
        try:
            del sdd_context.cube_structure_item_links_dictionary[cube_structure_item_link_id]
        except KeyError:
            pass

        # Remove from cube_structure_item_link_to_cube_link_map
        if cube_link_id:
            try:
                cube_structure_item_links = sdd_context.cube_structure_item_link_to_cube_link_map[cube_link_id]
                for cube_structure_item_link in cube_structure_item_links:
                    if cube_structure_item_link.cube_structure_item_link_id == cube_structure_item_link_id:
                        cube_structure_item_links.remove(cube_structure_item_link)
                        break
            except KeyError:
                pass

        messages.success(request, 'Link deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting link: {str(e)}')

    # Check the referer to determine which page to redirect back to
    referer = request.META.get('HTTP_REFERER', '')
    if 'edit-cube-structure-item-links' in referer:
        redirect_url = reverse('pybirdai:edit_cube_structure_item_links')
    else:
        # Preserve the filter parameters in the redirect for duplicate_primary_member_id_list
        params = request.GET.copy()
        params.pop('page', None)  # Remove page parameter to avoid invalid page numbers
        redirect_url = reverse('pybirdai:duplicate_primary_member_id_list')
        if params:
            redirect_url += f'?{params.urlencode()}'

    return redirect(redirect_url)

def delete_mapping_to_cube(request, mapping_to_cube_id):
    try:
        # Get the mapping_id and cube_mapping_id from the POST data
        mapping_id = request.POST.get('mapping_id')
        cube_mapping_id = request.POST.get('cube_mapping_id')

        if not all([mapping_id, cube_mapping_id]):
            raise ValueError("Missing required fields for deletion")

        # Get the item using the composite key fields
        item = MAPPING_TO_CUBE.objects.get(
            mapping_id=MAPPING_DEFINITION.objects.get(mapping_id=mapping_id),
            cube_mapping_id=cube_mapping_id
        )
        item.delete()
        messages.success(request, 'MAPPING_TO_CUBE deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting MAPPING_TO_CUBE: {str(e)}')
    return redirect('pybirdai:edit_mapping_to_cubes')

def delete_mapping_definition(request, mapping_id):
    return delete_item(request, MAPPING_DEFINITION, 'mapping_id', 'edit_mapping_definitions')

def delete_cube(request, cube_id):
    from urllib.parse import unquote
    decoded_cube_id = unquote(cube_id)
    return delete_item(request, CUBE, 'cube_id', 'output_layers', decoded_cube_id)

def list_lineage_files(request):
    lineage_dir = Path(settings.BASE_DIR) / 'results' / 'lineage'
    csv_files = []

    if lineage_dir.exists():
        csv_files = [f.name for f in lineage_dir.glob('*.csv')]

    return render(request, 'pybirdai/lineage_files.html', {'csv_files': csv_files})

def view_csv_file(request, filename):

    file_path = Path(settings.BASE_DIR) / 'results' / 'lineage' / filename

    if not file_path.exists() or not filename.endswith('.csv'):
        messages.error(request, 'File not found or invalid file type')
        return redirect('pybirdai:list_lineage_files')

    try:
        with open(file_path, 'r', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)  # Get the headers
            data = list(csv_reader)     # Get all rows

        # Paginate the results
        items_per_page = 50  # Adjust this number as needed
        paginator = Paginator(data, items_per_page)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        # Calculate some statistics
        total_rows = len(data)
        num_columns = len(headers)

        context = {
            'filename': filename,
            'headers': headers,
            'page_obj': page_obj,
            'total_rows': total_rows,
            'num_columns': num_columns,
            'start_index': (page_obj.number - 1) * items_per_page + 1,
            'end_index': min(page_obj.number * items_per_page, total_rows),
        }
        return render(request, 'pybirdai/view_csv.html', context)

    except Exception as e:
        messages.error(request, f'Error reading file: {str(e)}')
        return redirect('pybirdai:list_lineage_files')

def create_response_with_loading(request, task_title, success_message, return_url, return_link_text):
    html_response = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .loading-overlay {{
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background: rgba(255, 255, 255, 0.8);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    z-index: 9999;
                }}

                .loading-spinner {{
                    width: 50px;
                    height: 50px;
                    border: 5px solid #f3f3f3;
                    border-top: 5px solid #3498db;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                    margin-bottom: 20px;
                }}

                @keyframes spin {{
                    0% {{ transform: rotate(0deg); }}
                    100% {{ transform: rotate(360deg); }}
                }}

                .loading-message {{
                    font-size: 18px;
                    color: #333;
                }}

                .task-info {{
                    padding: 20px;
                    max-width: 600px;
                    margin: 0 auto;
                }}

                #success-message {{
                    display: none;
                    margin-top: 20px;
                    padding: 15px;
                    background-color: #d4edda;
                    border: 1px solid #c3e6cb;
                    border-radius: 4px;
                    color: #155724;
                }}
            </style>
        </head>
        <body>
            <div class="task-info">
                <h3>{task_title}</h3>
                <div id="loading-overlay" class="loading-overlay">
                    <div class="loading-spinner"></div>
                    <div class="loading-message">Please wait while the task completes...</div>
                </div>
                <div id="success-message">
                    <p>{success_message}</p>
                    <p>Go back to <a href="{return_url}">{return_link_text}</a></p>
                </div>
            </div>
            <script>
                document.addEventListener('DOMContentLoaded', function() {{
                    // Show loading immediately
                    document.getElementById('loading-overlay').style.display = 'flex';
                    document.getElementById('success-message').style.display = 'none';

                    // Start the task execution after a small delay to ensure loading is visible
                    setTimeout(() => {{
                        fetch(window.location.href + '?execute=true', {{
                            method: 'GET',
                            headers: {{
                                'X-Requested-With': 'XMLHttpRequest'
                            }}
                        }})
                        .then(response => response.json())
                        .then(data => {{
                            if (data.status === 'success') {{
                                // Hide loading and show success
                                document.getElementById('loading-overlay').style.display = 'none';
                                document.getElementById('success-message').style.display = 'block';
                            }} else {{
                                throw new Error('Task failed');
                            }}
                        }})
                        .catch(error => {{
                            console.error('Error:', error);
                            alert('An error occurred while processing the task: ' + error.message);
                        }});
                    }}, 100); // Small delay to ensure loading screen is visible
                }});
            </script>
        </body>
        </html>
    """

    # If this is the AJAX request to execute the task
    if request.GET.get('execute') == 'true':
        # Execute the actual task
        try:
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return HttpResponse(html_response)

def combinations(request):
    return paginated_modelformset_view(request, COMBINATION, 'pybirdai/combinations.html', order_by='combination_id')


def combination_items(request):
    # Get filter values from request
    variable_id = request.GET.get('variable_id', '')
    member_id = request.GET.get('member_id', '')

    # Start with all items and prefetch related fields
    queryset = COMBINATION_ITEM.objects.select_related(
        'combination_id',
        'variable_id',
        'member_id',
        'member_hierarchy'
    )

    # Get unique values for dropdowns using subqueries, ordered by their IDs
    unique_variable_ids = VARIABLE.objects.filter(
        variable_id__in=COMBINATION_ITEM.objects.values_list('variable_id__variable_id', flat=True)
    ).order_by('variable_id').values_list('variable_id', flat=True).distinct()

    unique_member_ids = MEMBER.objects.filter(
        member_id__in=COMBINATION_ITEM.objects.values_list('member_id__member_id', flat=True)
    ).order_by('member_id').values_list('member_id', flat=True).distinct()

    # Apply filters if provided
    if variable_id:
        queryset = queryset.filter(variable_id__variable_id=variable_id)
    if member_id:
        queryset = queryset.filter(member_id__member_id=member_id)

    # Add default ordering
    queryset = queryset.order_by('id')

    # Add pagination and formset creation
    page_number = request.GET.get('page', 1)
    paginator = Paginator(queryset, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(COMBINATION_ITEM, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, 'COMBINATION_ITEM updated successfully.')
            return redirect(request.get_full_path())
        else:
            messages.error(request, 'There was an error updating the COMBINATION_ITEM.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
        'unique_variable_ids': unique_variable_ids,
        'unique_member_ids': unique_member_ids,
        'selected_variable_id': variable_id,
        'selected_member_id': member_id,
    }
    return render(request, 'pybirdai/combination_items.html', context)


def output_layers(request):
    page_number = request.GET.get('page', 1)
    all_items = CUBE.objects.filter(cube_type='RC').order_by('cube_id')
    paginator = Paginator(all_items, 20)
    page_obj = paginator.get_page(page_number)

    ModelFormSet = modelformset_factory(CUBE, fields='__all__', extra=0)

    if request.method == 'POST':
        formset = ModelFormSet(request.POST, queryset=page_obj.object_list)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            messages.success(request, 'CUBE updated successfully.')
            return redirect(request.path)
        else:
            messages.error(request, 'There was an error updating the CUBE.')
    else:
        formset = ModelFormSet(queryset=page_obj.object_list)

    context = {
        'formset': formset,
        'page_obj': page_obj,
    }
    return render(request, 'pybirdai/output_layers.html', context)



def delete_combination(request, combination_id):
    try:
        combination = get_object_or_404(COMBINATION, combination_id=combination_id)
        combination.delete()
        messages.success(request, 'COMBINATION deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting COMBINATION: {str(e)}')
    return redirect('pybirdai:combinations')

def delete_combination_item(request, item_id):
    try:
        # Get the item using the combination_id, variable_id, and member_id
        # We need to get these from the form data since we don't have a primary key
        combination_id = request.POST.get('combination_id')
        variable_id = request.POST.get('variable_id')
        member_id = request.POST.get('member_id')

        if not all([combination_id, variable_id, member_id]):
            raise ValueError("Missing required fields for deletion")

        # Get the item using the composite key fields
        item = COMBINATION_ITEM.objects.get(
            combination_id=COMBINATION.objects.get(combination_id=combination_id),
            variable_id=VARIABLE.objects.get(variable_id=variable_id),
            member_id=MEMBER.objects.get(member_id=member_id)
        )
        item.delete()
        messages.success(request, 'COMBINATION_ITEM deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting COMBINATION_ITEM: {str(e)}')
    return redirect('pybirdai:combination_items')

class DuplicatePrimaryMemberIdListView(ListView):
    template_name = 'pybirdai/duplicate_primary_member_id_list.html'
    context_object_name = 'duplicate_links'
    paginate_by = 10  # Number of items per page

    def get_queryset(self):
        # First, find the combinations of primary_cube_id and primary_cube_variable_code
        # that have duplicates within their group
        duplicate_groups = CUBE_STRUCTURE_ITEM_LINK.objects.values(
            'cube_link_id__foreign_cube_id',
            'foreign_cube_variable_code',
            'cube_link_id__join_identifier'
        ).annotate(
            count=Count('cube_structure_item_link_id')
        ).filter(count__gt=1)

        # Then get all the CUBE_STRUCTURE_ITEM_LINK records that match these combinations
        return CUBE_STRUCTURE_ITEM_LINK.objects.filter(
            cube_link_id__foreign_cube_id__in=[
                group['cube_link_id__foreign_cube_id']
                for group in duplicate_groups
            ],
            foreign_cube_variable_code__in=[
                group['foreign_cube_variable_code']
                for group in duplicate_groups
            ],
            cube_link_id__join_identifier__in=[
                group['cube_link_id__join_identifier']
                for group in duplicate_groups
            ]
        ).select_related(
            'cube_link_id__foreign_cube_id',
            'cube_link_id__primary_cube_id',
            'foreign_cube_variable_code',
            'primary_cube_variable_code',
            'cube_link_id'
        ).order_by('cube_link_id')

class JoinIdentifierListView(ListView):
    template_name = 'pybirdai/join_identifier_list.html'
    context_object_name = 'join_identifiers'

    def get_queryset(self):
        return CUBE_LINK.objects.values_list('join_identifier', flat=True).distinct().order_by('join_identifier')

def duplicate_primary_member_id_list(request):
    # Get unique values for dropdowns
    foreign_cubes = CUBE_STRUCTURE_ITEM_LINK.objects.values_list(
        'cube_link_id__foreign_cube_id__cube_id',
        flat=True
    ).distinct().order_by('cube_link_id__foreign_cube_id__cube_id')

    primary_cubes = CUBE_STRUCTURE_ITEM_LINK.objects.values_list(
        'cube_link_id__primary_cube_id__cube_id',
        flat=True
    ).distinct().order_by('cube_link_id__primary_cube_id__cube_id')

    # First, find the combinations that have duplicates
    duplicate_groups = CUBE_STRUCTURE_ITEM_LINK.objects.values(
        'cube_link_id__foreign_cube_id',
        'foreign_cube_variable_code',
        'cube_link_id__join_identifier'
    ).annotate(
        count=Count('cube_structure_item_link_id')
    ).filter(count__gt=1)

    # Build the base queryset for duplicates
    queryset = CUBE_STRUCTURE_ITEM_LINK.objects.filter(
        cube_link_id__foreign_cube_id__in=[
            group['cube_link_id__foreign_cube_id']
            for group in duplicate_groups
        ],
        foreign_cube_variable_code__in=[
            group['foreign_cube_variable_code']
            for group in duplicate_groups
        ],
        cube_link_id__join_identifier__in=[
            group['cube_link_id__join_identifier']
            for group in duplicate_groups
        ]
    ).select_related(
        'cube_link_id__foreign_cube_id',
        'cube_link_id__primary_cube_id',
        'foreign_cube_variable_code',
        'primary_cube_variable_code',
        'cube_link_id'
    )

    # Apply filters if they exist in the request
    foreign_cube = request.GET.get('foreign_cube')
    primary_cube = request.GET.get('primary_cube')

    if foreign_cube:
        queryset = queryset.filter(cube_link_id__foreign_cube_id__cube_id__icontains=foreign_cube)
    if primary_cube:
        queryset = queryset.filter(cube_link_id__primary_cube_id__cube_id__icontains=primary_cube)

    # Pagination
    paginator = Paginator(queryset.order_by('cube_link_id'), 25)
    page = request.GET.get('page')
    duplicate_links = paginator.get_page(page)

    return render(request, 'pybirdai/duplicate_primary_member_id_list.html', {
        'duplicate_links': duplicate_links,
        'is_paginated': True,
        'page_obj': duplicate_links,
        'foreign_cubes': foreign_cubes,
        'primary_cubes': primary_cubes,
    })

def show_gaps(request):
    # Get the selected cube from the dropdown or default to None
    selected_cube_id = request.GET.get('cube_id')
    print(f"Selected cube_id: {selected_cube_id}")  # Direct print for immediate feedback

    # Get all cubes with cube_type = 'RC'
    rc_cubes = CUBE.objects.filter(cube_type='RC').order_by('cube_id')
    print(f"Number of RC cubes: {rc_cubes.count()}")

    context = {
        'cubes': rc_cubes,
        'selected_cube_id': selected_cube_id,
    }

    gaps = []

    # When selected_cube_id is empty string (All Cubes selected) or None, check all cubes
    if selected_cube_id:
        cubes_to_check = [get_object_or_404(CUBE, cube_id=selected_cube_id)]
    else:
        cubes_to_check = list(rc_cubes)
        print(f"Checking all cubes: {[cube.cube_id for cube in cubes_to_check]}")

    for cube in cubes_to_check:
        print(f"\nProcessing cube: {cube.cube_id}")

        # Get cube structure items
        cube_structure_items = CUBE_STRUCTURE_ITEM.objects.filter(
            cube_structure_id=cube.cube_structure_id
        ).order_by('order')
        print(f"Structure items found: {cube_structure_items.count()}")

        # Get cube links where this cube is the foreign cube
        cube_links = CUBE_LINK.objects.filter(foreign_cube_id=cube)
        print(f"Cube links found: {cube_links.count()}")

        if cube_links.exists():
            # Get all join identifiers
            join_identifiers = cube_links.values_list('join_identifier', flat=True).distinct()
            print(f"Join identifiers found: {list(join_identifiers)}")

            for join_identifier in join_identifiers:
                # Get links for this specific join identifier
                specific_links = cube_links.filter(join_identifier=join_identifier)
                print(f"\nChecking join identifier: {join_identifier}")
                print(f"Links for this identifier: {specific_links.count()}")

                # Get the variable IDs that already have links
                existing_variable_ids = CUBE_STRUCTURE_ITEM_LINK.objects.filter(
                    cube_link_id__in=specific_links
                ).values_list(
                    'foreign_cube_variable_code__variable_id',
                    flat=True
                ).distinct()
                print(f"Existing variable IDs: {list(existing_variable_ids)}")

                # Find missing links
                missing_items = cube_structure_items.exclude(
                    variable_id__in=existing_variable_ids
                )
                print(f"Missing items count: {missing_items.count()}")

                if missing_items.exists():
                    print(f"Found gaps for join identifier {join_identifier}")
                    gaps.append({
                        'join_identifier': join_identifier,
                        'cube_links': specific_links,
                        'missing_items': missing_items
                    })

    print(f"\nTotal gaps found: {len(gaps)}")
    context['gaps'] = gaps
    return render(request, 'pybirdai/show_gaps.html', context)

@require_http_methods(["POST"])
def delete_cube_structure_item_link(request, cube_structure_item_link_id):
    try:
        link = get_object_or_404(CUBE_STRUCTURE_ITEM_LINK, cube_structure_item_link_id=cube_structure_item_link_id)
        # Store the cube_link_id before deleting
        cube_link_id = link.cube_link_id.cube_link_id if link.cube_link_id else None
        link.delete()

        # Update the in-memory dictionaries
        sdd_context = SDDContext()

        # Remove from cube_structure_item_links_dictionary
        try:
            del sdd_context.cube_structure_item_links_dictionary[cube_structure_item_link_id]
        except KeyError:
            pass

        # Remove from cube_structure_item_link_to_cube_link_map
        if cube_link_id:
            try:
                cube_structure_item_links = sdd_context.cube_structure_item_link_to_cube_link_map[cube_link_id]
                for cube_structure_item_link in cube_structure_item_links:
                    if cube_structure_item_link.cube_structure_item_link_id == cube_structure_item_link_id:
                        cube_structure_item_links.remove(cube_structure_item_link)
                        break
            except KeyError:
                pass

        messages.success(request, 'Link deleted successfully.')
    except Exception as e:
        messages.error(request, f'Error deleting link: {str(e)}')

    # Check the referer to determine which page to redirect back to
    referer = request.META.get('HTTP_REFERER', '')
    if 'edit-cube-structure-item-links' in referer:
        redirect_url = reverse('pybirdai:edit_cube_structure_item_links')
    else:
        # Preserve the filter parameters in the redirect for duplicate_primary_member_id_list
        params = request.GET.copy()
        params.pop('page', None)  # Remove page parameter to avoid invalid page numbers
        redirect_url = reverse('pybirdai:duplicate_primary_member_id_list')
        if params:
            redirect_url += f'?{params.urlencode()}'

    return redirect(redirect_url)

@require_http_methods(["POST"])
def add_cube_structure_item_link(request):
    try:
        # Get the user-provided ID
        cube_structure_item_link_id = request.POST['cube_structure_item_link_id']

        # Get the CUBE_LINK instance
        cube_link = get_object_or_404(CUBE_LINK, cube_link_id=request.POST['cube_link_id'])

        # Get the CUBE_STRUCTURE_ITEM instances
        foreign_cube_variable = get_object_or_404(CUBE_STRUCTURE_ITEM, id=request.POST['foreign_cube_variable_code'])
        primary_cube_variable = get_object_or_404(CUBE_STRUCTURE_ITEM, id=request.POST['primary_cube_variable_code'])

        # Create the new link with the user-provided ID
        new_link = CUBE_STRUCTURE_ITEM_LINK.objects.create(
            cube_structure_item_link_id=cube_structure_item_link_id,
            cube_link_id=cube_link,
            foreign_cube_variable_code=foreign_cube_variable,
            primary_cube_variable_code=primary_cube_variable
        )

        # Update the in-memory dictionaries
        sdd_context = SDDContext()

        # Add to cube_structure_item_links_dictionary
        sdd_context.cube_structure_item_links_dictionary[cube_structure_item_link_id] = new_link

        # Add to cube_structure_item_link_to_cube_link_map
        try:
            sdd_context.cube_structure_item_link_to_cube_link_map[cube_link.cube_link_id].append(new_link)
        except KeyError:
            sdd_context.cube_structure_item_link_to_cube_link_map[cube_link.cube_link_id] = [new_link]

        messages.success(request, 'New cube structure item link created successfully.')
    except Exception as e:
        messages.error(request, f'Error creating link: {str(e)}')

    return redirect('pybirdai:edit_cube_structure_item_links')

@require_http_methods(["POST"])
def add_cube_link(request):
    try:
        # Get the cube instances
        primary_cube = get_object_or_404(CUBE, cube_id=request.POST['primary_cube_id'])
        foreign_cube = get_object_or_404(CUBE, cube_id=request.POST['foreign_cube_id'])

        # Create the new cube link
        new_link = CUBE_LINK.objects.create(
            cube_link_id=request.POST['cube_link_id'],
            code=request.POST.get('code'),
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            order_relevance=request.POST.get('order_relevance'),
            primary_cube_id=primary_cube,
            foreign_cube_id=foreign_cube,
            cube_link_type=request.POST.get('cube_link_type'),
            join_identifier=request.POST.get('join_identifier')
        )

        # Update the in-memory dictionaries
        sdd_context = SDDContext()

        # Add to cube_link_dictionary
        sdd_context.cube_link_dictionary[new_link.cube_link_id] = new_link

        # Add to cube_link_to_foreign_cube_map
        sdd_context.cube_link_to_foreign_cube_map[new_link.cube_link_id] = new_link.foreign_cube_id

        # Add to cube_link_to_join_identifier_map
        if new_link.join_identifier:
            sdd_context.cube_link_to_join_identifier_map[new_link.cube_link_id] = new_link.join_identifier

        # Add to cube_link_to_join_for_report_id_map
        # Note: This might need additional logic depending on how join_for_report_id is determined
        if new_link.join_identifier:
            sdd_context.cube_link_to_join_for_report_id_map[new_link.cube_link_id] = new_link.join_identifier

        messages.success(request, 'New cube link created successfully.')
    except Exception as e:
        messages.error(request, f'Error creating cube link: {str(e)}')

    return redirect('pybirdai:edit_cube_links')

def create_variable_mapping(request):
    if request.method == 'POST':
        try:
            # Create new variable mapping
            variable_mapping = VARIABLE_MAPPING(
                name=request.POST.get('name'),
                code=request.POST.get('code'),
                variable_mapping_id=request.POST.get('variable_mapping_id'),
                maintenance_agency_id=MAINTENANCE_AGENCY.objects.get(
                    maintenance_agency_id=request.POST.get('maintenance_agency_id')
                )
            )
            variable_mapping.save()
            messages.success(request, 'Variable mapping created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating variable mapping: {str(e)}')
    return redirect('pybirdai:edit_variable_mappings')

def create_member_mapping(request):
    if request.method == 'POST':
        try:
            maintenance_agency = None
            if request.POST.get('maintenance_agency_id'):
                maintenance_agency = get_object_or_404(MAINTENANCE_AGENCY, maintenance_agency_id=request.POST.get('maintenance_agency_id'))

            member_mapping = MEMBER_MAPPING(
                name=request.POST.get('name'),
                code=request.POST.get('code'),
                maintenance_agency_id=maintenance_agency,
                member_mapping_id=request.POST.get('member_mapping_id')
            )
            member_mapping.save()

            messages.success(request, 'Member Mapping created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating Member Mapping: {str(e)}')

    return redirect('pybirdai:edit_member_mappings')

def add_member_mapping_item(request):
    if request.method == 'POST':
        try:
            # Extract data from POST request
            is_source = request.POST.get('is_source', '').lower()  # Convert to lowercase for consistency
            member_id = request.POST.get('member_id')
            variable_id = request.POST.get('variable_id')
            member_mapping_row = request.POST.get('member_mapping_row')
            member_mapping_id = request.POST.get('member_mapping_id')
            member_hierarchy_id = request.POST.get('member_hierarchy')
            valid_from = request.POST.get('valid_from') or None
            valid_to = request.POST.get('valid_to') or None

            # Get related objects
            member = get_object_or_404(MEMBER, member_id=member_id) if member_id else None
            variable = get_object_or_404(VARIABLE, variable_id=variable_id) if variable_id else None
            member_mapping = get_object_or_404(MEMBER_MAPPING, member_mapping_id=member_mapping_id) if member_mapping_id else None
            member_hierarchy = get_object_or_404(MEMBER_HIERARCHY, member_hierarchy_id=member_hierarchy_id) if member_hierarchy_id else None

            # Create new member mapping item
            MEMBER_MAPPING_ITEM.objects.create(
                is_source=is_source,
                member_id=member,
                variable_id=variable,
                member_mapping_row=member_mapping_row,
                member_mapping_id=member_mapping,
                member_hierarchy=member_hierarchy,
                valid_from=valid_from,
                valid_to=valid_to
            )

            messages.success(request, 'Member Mapping Item created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating Member Mapping Item: {str(e)}')

    return redirect('pybirdai:edit_member_mapping_items')

def create_mapping_to_cube(request):
    if request.method == 'POST':
        try:
            # Get form data
            mapping_id = request.POST.get('mapping_id')
            cube_mapping = request.POST.get('cube_mapping_id')
            valid_from = request.POST.get('valid_from')
            valid_to = request.POST.get('valid_to')

            # Get the mapping definition object
            mapping = get_object_or_404(MAPPING_DEFINITION, mapping_id=mapping_id)

            # Create new mapping to cube
            mapping_to_cube = MAPPING_TO_CUBE(
                mapping_id=mapping,
                cube_mapping_id=cube_mapping,
                valid_from=valid_from if valid_from else None,
                valid_to=valid_to if valid_to else None
            )
            mapping_to_cube.save()

            messages.success(request, 'New mapping to cube created successfully.')
        except Exception as e:
            messages.error(request, f'Error creating mapping to cube: {str(e)}')

    return redirect('pybirdai:edit_mapping_to_cubes')

def view_member_mapping_items_by_row(request):
    # Get all member mappings for the dropdown
    member_mappings = MEMBER_MAPPING.objects.all().order_by('member_mapping_id')

    # Get the selected mapping from the query parameters
    selected_mapping = request.GET.get('member_mapping', '')

    items_by_row = {}
    source_variables = set()  # Track source variables
    target_variables = set()  # Track target variables

    if selected_mapping:
        # Get all items for the selected mapping
        items = MEMBER_MAPPING_ITEM.objects.filter(member_mapping_id=selected_mapping)

        # First pass: collect variables and organize items by row
        for item in items:
            row = item.member_mapping_row
            if row not in items_by_row:
                items_by_row[row] = {'items': {}}

            # Add item to the row dictionary, using variable as key
            if item.variable_id:
                var_id = item.variable_id.variable_id
                items_by_row[row]['items'][var_id] = item

                # Track whether this variable is used as source or target
                if item.is_source.lower() == 'true':
                    source_variables.add(var_id)
                else:
                    target_variables.add(var_id)

    # Convert to sorted lists - source variables first, then target variables
    source_variables = sorted(list(source_variables))
    target_variables = sorted(list(target_variables))

    # Convert items_by_row to a sorted list of tuples based on numeric row value
    sorted_items = sorted(items_by_row.items(), key=lambda x: int(x[0]))
    items_by_row = dict(sorted_items)

    context = {
        'member_mappings': member_mappings,
        'selected_mapping': selected_mapping,
        'items_by_row': items_by_row,
        'source_variables': source_variables,
        'target_variables': target_variables,
    }

    return render(request, 'pybirdai/view_member_mapping_items_by_row.html', context)

def export_database_to_csv(request):
    if request.method == 'GET':
        return render(request, 'pybirdai/export_database.html')
    elif request.method == 'POST':
        # Create a zip file in memory
        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="database_export.zip"'

        # Get all model classes from bird_meta_data_model
        valid_table_names = set()
        model_map = {}  # Store model classes for reference
        for name, obj in inspect.getmembers(bird_meta_data_model):
            if inspect.isclass(obj) and issubclass(obj, models.Model) and obj != models.Model:
                valid_table_names.add(obj._meta.db_table)
                model_map[obj._meta.db_table] = obj

        with zipfile.ZipFile(response, 'w') as zip_file:
            # Get all table names from SQLite
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' AND name NOT LIKE 'django_%'")
                tables = cursor.fetchall()

            # Export each table to a CSV file
            for table in tables:
                is_meta_data_table = False
                table_name = table[0]

                if table_name in valid_table_names:
                    is_meta_data_table = True
                    # Get the model class for this table
                    model_class = model_map[table_name]

                    # Get fields in the order they're defined in the model
                    fields = model_class._meta.fields
                    headers = []
                    db_headers = []
                    for field in fields:
                        # Skip the id field
                        if field.name == 'id':
                            continue
                        headers.append(field.name.upper())  # Convert header to uppercase
                        # If it's a foreign key, append _id for the actual DB column
                        if isinstance(field, models.ForeignKey):
                            db_headers.append(f"{field.name}_id")
                        else:
                            db_headers.append(field.name)

                    # Create CSV in memory
                    csv_content = []
                    csv_content.append(','.join(headers))

                    # Get data with escaped column names and ordered by primary key
                    with connection.cursor() as cursor:
                        escaped_headers = [f'"{h}"' if h == 'order' else h for h in db_headers]
                        # Get primary key column name
                        cursor.execute(f"PRAGMA table_info({table_name})")
                        table_info = cursor.fetchall()
                        pk_column = None
                        for col in table_info:
                            if col[5] == 1:  # 5 is the index for pk flag in table_info
                                pk_column = col[1]  # 1 is the index for column name
                                break

                        # Build ORDER BY clause
                        order_by = f"ORDER BY {pk_column}" if pk_column else "ORDER BY rowid"  # rowid is always available in SQLite
                        cursor.execute(f"SELECT {','.join(escaped_headers)} FROM {table_name} {order_by}")
                        rows = cursor.fetchall()

                        for row in rows:
                            # Convert all values to strings and handle None values
                            csv_row = [str(val) if val is not None else '' for val in row]
                            # Escape commas and quotes in values
                            processed_row = []
                            for val in csv_row:
                                if ',' in val or '"' in val:
                                    escaped_val = val.replace('"', '""')
                                    processed_row.append(f'"{escaped_val}"')
                                else:
                                    processed_row.append(val)
                            csv_content.append(','.join(processed_row))
                else:
                    # Fallback for tables without models
                    with connection.cursor() as cursor:
                        # Get column names
                        cursor.execute(f"SELECT * FROM {table_name} LIMIT 0")
                        headers = []
                        column_names = []
                        for desc in cursor.description:
                            # Skip the id column
                            if desc[0].lower() != 'id':
                                headers.append(desc[0].upper())
                                column_names.append(desc[0])

                        # Get data with escaped column names and ordered by rowid
                        escaped_headers = [f'"{h.lower()}"' if h.lower() == 'order' else h.lower() for h in column_names]
                        cursor.execute(f"SELECT {','.join(escaped_headers)} FROM {table_name} ORDER BY rowid")
                        rows = cursor.fetchall()

                        # Create CSV in memory
                        csv_content = []
                        csv_content.append(','.join(headers))
                        for row in rows:
                            # Convert all values to strings and handle None values
                            csv_row = [str(val) if val is not None else '' for val in row]
                            # Escape commas and quotes in values
                            processed_row = []
                            for val in csv_row:
                                if ',' in val or '"' in val:
                                    escaped_val = val.replace('"', '""')
                                    processed_row.append(f'"{escaped_val}"')
                                else:
                                    processed_row.append(val)
                            csv_content.append(','.join(processed_row))

                # Add CSV to zip file
                if is_meta_data_table:
                    zip_file.writestr(f"{table_name.replace('pybirdai_', '')}.csv", '\n'.join(csv_content))
                else:
                    zip_file.writestr(f"{table_name.replace('pybirdai_', 'bird_')}.csv", '\n'.join(csv_content))

        return response

def bird_diffs_and_corrections(request):
    """
    View function for displaying BIRD diffs and corrections page.
    """
    return render(request, 'pybirdai/bird_diffs_and_corrections.html')

def convert_ldm_to_sdd_hierarchies(request):
    """View for converting LDM hierarchies to SDD hierarchies."""
    if request.GET.get('execute') == 'true':
        try:
            RunConvertLDMToSDDHierarchies.run_convert_hierarchies()
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return create_response_with_loading(
        request,
        'Converting LDM Hierarchies to SDD Hierarchies',
        'Successfully converted LDM hierarchies to SDD hierarchies.',
        reverse('pybirdai:bird_diffs_and_corrections'),
        'BIRD Export Diffs and Corrections'
    )

def view_ldm_to_sdd_results(request):
    """View for displaying the LDM to SDD hierarchy conversion results."""
    results_dir = os.path.join(settings.BASE_DIR, 'results', 'ldm_to_sdd_hierarchies')

    # Read the CSV files
    csv_data = {}
    for filename in ['member_hierarchy.csv', 'member_hierarchy_node.csv', 'missing_members.csv']:
        filepath = os.path.join(results_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', newline='') as f:
                reader = csv.reader(f)
                headers = next(reader)  # Get headers
                rows = list(reader)     # Get data rows
                csv_data[filename] = {'headers': headers, 'rows': rows}

    return render(request, 'pybirdai/view_ldm_to_sdd_results.html', {'csv_data': csv_data})

def import_members_from_csv(request):
    if request.method == 'GET':
        return render(request, 'pybirdai/import_members.html')
    elif request.method == 'POST':
        try:
            csv_file = request.FILES.get('csvFile')
            if not csv_file:
                return HttpResponseBadRequest('No file was uploaded')

            if not csv_file.name.endswith('.csv'):
                return HttpResponseBadRequest('File must be a CSV')

            # Read the CSV file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Validate headers
            required_fields = {'MEMBER_ID', 'CODE', 'NAME', 'DESCRIPTION', 'DOMAIN_ID'}
            headers = set(reader.fieldnames)
            if not required_fields.issubset(headers):
                missing = required_fields - headers
                return HttpResponseBadRequest(f'Missing required columns: {", ".join(missing)}')

            # Process each row
            members_to_create = []
            for row in reader:
                try:
                    # Look up the domain
                    domain = DOMAIN.objects.get(domain_id=row['DOMAIN_ID'])

                    member = MEMBER(
                        member_id=row['MEMBER_ID'],
                        code=row['CODE'],
                        name=row['NAME'],
                        description=row['DESCRIPTION'],
                        domain_id=domain
                    )
                    members_to_create.append(member)
                except DOMAIN.DoesNotExist:
                    return HttpResponseBadRequest(f'Domain with ID {row["DOMAIN_ID"]} not found')

            # Bulk create the members
            if members_to_create:
                MEMBER.objects.bulk_create(members_to_create)

            return JsonResponse({'message': 'Import successful', 'count': len(members_to_create)})

        except Exception as e:
            return HttpResponseBadRequest(str(e))

def import_variables_from_csv(request):
    if request.method == 'GET':
        return render(request, 'pybirdai/import_variables.html')
    elif request.method == 'POST':
        try:
            csv_file = request.FILES.get('csvFile')
            if not csv_file:
                return HttpResponseBadRequest('No file was uploaded')

            if not csv_file.name.endswith('.csv'):
                return HttpResponseBadRequest('File must be a CSV')

            # Read the CSV file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            # Validate headers
            required_fields = {'VARIABLE_ID', 'CODE', 'NAME', 'DESCRIPTION', 'DOMAIN_ID'}
            headers = set(reader.fieldnames)
            if not required_fields.issubset(headers):
                missing = required_fields - headers
                return HttpResponseBadRequest(f'Missing required columns: {", ".join(missing)}')

            # Get SDDContext instance
            sdd_context = SDDContext()

            # Process each row
            variables_to_create = []
            for row in reader:
                try:
                    # Look up the domain
                    domain = DOMAIN.objects.get(domain_id=row['DOMAIN_ID'])

                    variable = VARIABLE(
                        variable_id=row['VARIABLE_ID'],
                        code=row['CODE'],
                        name=row['NAME'],
                        description=row['DESCRIPTION'],
                        domain_id=domain
                    )
                    variables_to_create.append(variable)
                except DOMAIN.DoesNotExist:
                    return HttpResponseBadRequest(f'Domain with ID {row["DOMAIN_ID"]} not found')

            # Bulk create the variables
            if variables_to_create:
                created_variables = VARIABLE.objects.bulk_create(variables_to_create)

                # Update SDDContext variable dictionary
                for variable in created_variables:
                    sdd_context.variable_dictionary[variable.variable_id] = variable

            return JsonResponse({'message': 'Import successful', 'count': len(variables_to_create)})

        except Exception as e:
            return HttpResponseBadRequest(str(e))

def run_create_executable_filters_from_db(request):
    if request.GET.get('execute') == 'true':
        app_config = RunCreateExecutableFilters('pybirdai', 'birds_nest')
        app_config.run_create_executable_filters_from_db()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Executable Filters from Database (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Create executable filters from database process completed successfully",
        '/pybirdai/create-transformation-rules-in-python',
        "Create Transformations Rules in Python"
    )

def run_create_python_joins_from_db(request):
    if request.GET.get('execute') == 'true':
        app_config = RunCreateExecutableJoins('pybirdai', 'birds_nest')
        app_config.create_python_joins_from_db()
        return JsonResponse({'status': 'success'})

    return create_response_with_loading(
        request,
        "Creating Python Joins from Database (approx 1 minute on a fast desktop, dont press the back button on this web page)",
        "Created Executable Joins from Database in Python",
        '/pybirdai/create-transformation-rules-in-python',
        "Create Transformations Rules in Python"
    )


def return_semantic_integration_menu(request: Any, mapping_id: str = "") -> Any:
    """Returns semantic integration menu view.

    Args:
        request: HTTP request object
        mapping_id: Optional mapping identifier

    Returns:
        Rendered template response
    """
    logger.info(f"Handling semantic integration menu request for mapping ID: {mapping_id}")
    domains = None
    selected_mapping = request.GET.get('mapping_id', mapping_id)

    mtcs = MAPPING_TO_CUBE.objects.all()
    logger.debug(f"Found {len(mtcs)} MAPPING_TO_CUBE records")
    maps = [mtc.cube_mapping_id for mtc in mtcs if 'M_F_01_01_REF_FINREP 3_0' == mtc.cube_mapping_id]

    mapping_definitions = MAPPING_DEFINITION.objects.all()
    results = build_mapping_results(mapping_definitions)
    context = {"mapping_data": {k: v for k, v in results.items() if v["has_member_mapping"]}}

    reference_variables = get_reference_variables()
    keys = sorted(reference_variables.keys())
    reference_variables = {k:reference_variables[k] for k in keys}
    context["available_variables"] = reference_variables

    if selected_mapping:
        logger.info(f"Processing selected mapping: {selected_mapping}")
        map_def = MAPPING_DEFINITION.objects.get(code=selected_mapping)
        member_mapping_items = MEMBER_MAPPING_ITEM.objects.filter(member_mapping_id=map_def.member_mapping_id.code)
        var_items = VARIABLE_MAPPING_ITEM.objects.filter(variable_mapping_id=map_def.variable_mapping_id)

        temp_items, unique_set, source_target = process_member_mappings(member_mapping_items, var_items)
        serialized_items_2 = {row_id: row_data['items'] for row_id, row_data in temp_items.items()}
        table_data = create_table_data(serialized_items_2, unique_set)


        context.update({
            'table_data': table_data,
            "selected_mapping": selected_mapping,
            "uniques":unique_set,
            "domains":domains,
            "uniques_sources":{k:v for k,v in unique_set.items() if k in source_target["source"]},
            "uniques_targets":{k:v for k,v in unique_set.items() if k in source_target["target"]},
        })

    return render(request, 'pybirdai/return_semantic_integrations.html', context)


def add_variable_endpoint(request: Any) -> JsonResponse:
    """Endpoint for adding variables.

    Args:
        request: HTTP request object

    Returns:
        JSON response with status
    """
    logger.info("Handling add variable endpoint request")
    if request.method != "POST":
        logger.warning("Invalid request method")
        return HttpResponseBadRequest('Invalid request method')

    try:
        data = json.loads(request.body)
        orig_mapping_id = data.get('mapping_id')
        member_mapping_row = data.get('member_mapping_row')
        variable = data.get('variable')
        members = data.get('members', [])
        is_source = data.get('is_source', 'true')

        # Get the variable object
        variable_obj = VARIABLE.objects.get(variable_id=variable)

        # Get timestamp suffix
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Copy existing mapping if it exists
        if orig_mapping_id:
            orig_mapping = MAPPING_DEFINITION.objects.get(mapping_id=orig_mapping_id)

            # Extract base IDs without timestamp if they exist
            member_mapping_base_id = orig_mapping.member_mapping_id.member_mapping_id.split('__')[0] if '__' in orig_mapping.member_mapping_id.member_mapping_id else orig_mapping.member_mapping_id.member_mapping_id
            variable_mapping_base_id = orig_mapping.variable_mapping_id.variable_mapping_id.split('__')[0] if '__' in orig_mapping.variable_mapping_id.variable_mapping_id else orig_mapping.variable_mapping_id.variable_mapping_id
            mapping_base_id = orig_mapping.mapping_id.split('__')[0] if '__' in orig_mapping.mapping_id else orig_mapping.mapping_id

            # Copy member mapping
            new_member_mapping = MEMBER_MAPPING.objects.create(
                member_mapping_id=f"{member_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                code=f"{member_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                name=f"{orig_mapping.member_mapping_id.name} ({timestamp})"
            )

            # Copy variable mapping
            new_variable_mapping = VARIABLE_MAPPING.objects.create(
                variable_mapping_id=f"{variable_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                code=f"{variable_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                name=f"{orig_mapping.variable_mapping_id.name} ({timestamp})"
            )

            # Copy existing variable mapping items
            existing_variable_items = VARIABLE_MAPPING_ITEM.objects.filter(variable_mapping_id=orig_mapping.variable_mapping_id)
            for item in existing_variable_items:
                new_variable_item = VARIABLE_MAPPING_ITEM.objects.create(
                    variable_mapping_id=new_variable_mapping,
                    variable_id=item.variable_id,
                    is_source=item.is_source
                )
                logger.info(f"I created new variable mapping item: {new_variable_item.id}")

            new_variable_item = VARIABLE_MAPPING_ITEM.objects.create(
                variable_mapping_id=new_variable_mapping,
                variable_id=variable_obj,
                is_source=is_source
            )

            logger.info(f"I created new variable mapping item: {new_variable_item.id}")

            # Copy mapping definition
            mapping_def = MAPPING_DEFINITION.objects.create(
                mapping_id=f"{mapping_base_id}".split("__")[0]+f"__{timestamp}",
                code=f"{mapping_base_id}".split("__")[0]+f"__{timestamp}",
                name=f"{orig_mapping.name} ({timestamp})",
                member_mapping_id=new_member_mapping,
                variable_mapping_id=new_variable_mapping
            )

            # Copy existing member mapping items
            existing_items = MEMBER_MAPPING_ITEM.objects.filter(member_mapping_id=orig_mapping.member_mapping_id)
            for item in existing_items:
                MEMBER_MAPPING_ITEM.objects.create(
                    member_mapping_id=new_member_mapping,
                    member_mapping_row=item.member_mapping_row,
                    variable_id=item.variable_id,
                    member_id=item.member_id,
                    is_source=item.is_source
                )

        else:
            # Create new mappings
            new_member_mapping = MEMBER_MAPPING.objects.create(
                member_mapping_id=f"MM_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                code=f"MM_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                name=f"Member mapping for {variable_obj.code}"
            )

            new_variable_mapping = VARIABLE_MAPPING.objects.create(
                variable_mapping_id=f"VM_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                code=f"VM_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                name=f"Variable mapping for {variable_obj.code}"
            )

            mapping_def = MAPPING_DEFINITION.objects.create(
                mapping_id=f"MAP_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                code=f"MAP_{variable_obj.code}".split("__")[0]+f"__{timestamp}",
                name=f"Mapping for {variable_obj.code}",
                member_mapping_id=new_member_mapping,
                variable_mapping_id=new_variable_mapping
            )

        # Add new member mapping items
        member_mapping_items = []
        for member_id in members:
            if member_id != "None":
                member_obj = MEMBER.objects.get(member_id=member_id)
                mapping_item = MEMBER_MAPPING_ITEM(
                    member_mapping_id=new_member_mapping,
                    member_mapping_row=member_mapping_row,
                    variable_id=variable_obj,
                    member_id=member_obj,
                    is_source=is_source
                )
                member_mapping_items.append(mapping_item)

        # Bulk create member mapping items
        MEMBER_MAPPING_ITEM.objects.bulk_create(member_mapping_items)

        # Create mapping to cube with version suffix
        old_mappings = MAPPING_TO_CUBE.objects.filter(mapping_id=mapping_def)
        if old_mappings.exists():
            latest = old_mappings.latest('cube_mapping_id')
            version = int(latest.cube_mapping_id.split('_v')[-1]) + 1
            new_mapping_code = f"{latest.cube_mapping_id.split('_v')[0]}_v{version}"
        else:
            new_mapping_code = f"{mapping_def.code}_v1"

        MAPPING_TO_CUBE.objects.create(
            mapping_id=mapping_def,
            cube_mapping_id=new_mapping_code
        )

        logger.info("Variable and members added successfully")
        return JsonResponse({'status': 'success'})

    except Exception as e:
        logger.error(f"Error adding variable: {str(e)}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)})

def edit_mapping_endpoint(request: Any) -> JsonResponse:
    """Endpoint for editing mappings.

    Args:
        request: HTTP request object

    Returns:
        JSON response with status
    """
    logger.info("Handling edit mapping endpoint request")
    if request.method != "POST":
        logger.warning("Invalid request method")
        return HttpResponseBadRequest('Invalid request method')

    try:
        data = json.loads(request.body)
        orig_mapping_id = data.get('mapping_id')
        source_data = data.get('source_data', {})
        target_data = data.get('target_data', {})

        print(source_data,target_data)

        # Get timestamp for new instances
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Get existing mapping if available
        if orig_mapping_id:
            with transaction.atomic():
                orig_mapping = MAPPING_DEFINITION.objects.get(mapping_id=orig_mapping_id)

                # Extract base IDs without timestamp if they exist
                member_mapping_base_id = orig_mapping.member_mapping_id.member_mapping_id.split('__')[0] if '__' in orig_mapping.member_mapping_id.member_mapping_id else orig_mapping.member_mapping_id.member_mapping_id
                variable_mapping_base_id = orig_mapping.variable_mapping_id.variable_mapping_id.split('__')[0] if '__' in orig_mapping.variable_mapping_id.variable_mapping_id else orig_mapping.variable_mapping_id.variable_mapping_id
                mapping_base_id = orig_mapping.mapping_id.split('__')[0] if '__' in orig_mapping.mapping_id else orig_mapping.mapping_id

                # Copy member mapping
                new_member_mapping = MEMBER_MAPPING.objects.create(
                    member_mapping_id=f"{member_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    code=f"{member_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    name=f"{orig_mapping.member_mapping_id.name} ({timestamp})"
                )
                logger.info(f"I created new member mapping with ID: {new_member_mapping.member_mapping_id}")

                # Copy variable mapping
                new_variable_mapping = VARIABLE_MAPPING.objects.create(
                    variable_mapping_id=f"{variable_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    code=f"{variable_mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    name=f"{orig_mapping.variable_mapping_id.name} ({timestamp})"
                )
                logger.info(f"I created new variable mapping with ID: {new_variable_mapping.variable_mapping_id}")

                # Copy existing variable mapping items
                existing_variable_items = VARIABLE_MAPPING_ITEM.objects.filter(variable_mapping_id=orig_mapping.variable_mapping_id)
                for item in existing_variable_items:
                    new_variable_item = VARIABLE_MAPPING_ITEM.objects.create(
                        variable_mapping_id=new_variable_mapping,
                        variable_id=item.variable_id,
                        is_source=item.is_source
                    )
                    logger.info(f"I created new variable mapping item: {new_variable_item.id}")

                # Copy mapping definition
                mapping_def = MAPPING_DEFINITION.objects.create(
                    mapping_id=f"{mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    code=f"{mapping_base_id}".split("__")[0]+f"__{timestamp}",
                    name=f"{orig_mapping.name} ({timestamp})",
                    member_mapping_id=new_member_mapping,
                    variable_mapping_id=new_variable_mapping
                )
                logger.info(f"I created new mapping definition with ID: {mapping_def.mapping_id}")

                # Copy existing member mapping items
                existing_items = MEMBER_MAPPING_ITEM.objects.filter(member_mapping_id=orig_mapping.member_mapping_id)
                for item in existing_items:
                    new_item = MEMBER_MAPPING_ITEM.objects.create(
                        member_mapping_id=new_member_mapping,
                        member_mapping_row=item.member_mapping_row,
                        variable_id=item.variable_id,
                        member_id=item.member_id,
                        is_source=item.is_source
                    )
                    logger.info(f"I created new member mapping item for row {new_item.member_mapping_row}")

                last_member_mapping_row = str(max(int(item.member_mapping_row) for item in existing_items)+1)

                for variable_,member_ in zip(source_data["variabless"],source_data["members"]):
                    variable_id = variable_.split(" ")[-1].strip("(").rstrip(")")
                    variable_obj = VARIABLE.objects.get(code=variable_id)
                    member_obj = MEMBER.objects.get(member_id=member_)

                    new_member_item = MEMBER_MAPPING_ITEM.objects.create(
                        member_mapping_id=new_member_mapping,
                        member_mapping_row=last_member_mapping_row,
                        variable_id=variable_obj,
                        member_id=member_obj,
                        is_source=True
                    )
                    logger.info(f"I created new member mapping item for row {last_member_mapping_row}")

                for variable_,member_ in zip(target_data["variablses"],target_data["members"]):
                    variable_id = variable_.split(" ")[-1].strip("(").rstrip(")")
                    variable_obj = VARIABLE.objects.get(variable_id=variable_id)
                    member_obj = MEMBER.objects.get(member_id=member_)

                    new_member_item = MEMBER_MAPPING_ITEM.objects.create(
                        member_mapping_id=new_member_mapping,
                        member_mapping_row=last_member_mapping_row,
                        variable_id=variable_obj,
                        member_id=member_obj,
                        is_source=False
                    )
                    logger.info(f"I created new member mapping item for row {last_member_mapping_row}")


        with transaction.atomic():

            # Create mapping to cube with version suffix
            old_mappings = MAPPING_TO_CUBE.objects.filter(mapping_id=mapping_def)
            if old_mappings.exists():
                latest = old_mappings.latest('cube_mapping_id')
                version = int(latest.cube_mapping_id.split('_v')[-1]) + 1
                new_mapping_code = f"{latest.cube_mapping_id.split('_v')[0]}_v{version}"
            else:
                new_mapping_code = f"{mapping_def.code}_v1"

            mapping_to_cube = MAPPING_TO_CUBE.objects.create(
                mapping_id=mapping_def,
                cube_mapping_id=new_mapping_code
            )
            logger.info(f"I created new mapping to cube with ID: {mapping_to_cube.cube_mapping_id}")

        logger.info("Mapping updated successfully")
        return JsonResponse({'status': 'success'})

    except Exception as e:
        logger.error(f"Error updating mapping: {str(e)}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)})

def get_domain_members(request, variable_id:str=""):
    """Get domain members for a variable.

    Args:
        request: HTTP request object
        variable_id: ID of variable to get members for

    Returns:
        JSON response with members data
    """
    logger.info("Handling get domain members request")
    try:
        if not variable_id:
            logger.warning("No variable ID provided")
            return JsonResponse({'status': 'error', 'message': 'Variable ID required'})

        variable = VARIABLE.objects.get(variable_id=variable_id)
        domain = variable.domain_id
        members = MEMBER.objects.filter(domain_id=domain)

        member_data = []
        for member in members:
            member_data.append({
                'member_id': member.member_id,
                'code': member.code,
                'name': member.name
            })

        logger.info(f"Found {len(member_data)} members for variable {variable_id}")
        return JsonResponse({
            'status': 'success',
            'members': member_data
        })

    except VARIABLE.DoesNotExist:
        logger.error(f"Variable {variable_id} not found")
        return JsonResponse({
            'status': 'error',
            'message': f'Variable {variable_id} not found'
        })
    except Exception as e:
        logger.error(f"Error getting domain members: {str(e)}", exc_info=True)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })

def get_mapping_details(request, mapping_id):
    """Get mapping definition and related details.

    Args:
        request: HTTP request object
        mapping_id: ID of mapping to get details for

    Returns:
        JSON response with mapping data
    """
    logger.info(f"Handling get mapping details request for mapping {mapping_id}")
    try:
        # Get mapping definition
        mapping_def = MAPPING_DEFINITION.objects.get(mapping_id=mapping_id)

        # Get variable mapping and items
        variable_mapping = mapping_def.variable_mapping_id
        variable_mapping_items = VARIABLE_MAPPING_ITEM.objects.filter(
            variable_mapping_id=variable_mapping
        )

        # Get member mapping and items
        member_mapping = mapping_def.member_mapping_id
        member_mapping_items = MEMBER_MAPPING_ITEM.objects.filter(
            member_mapping_id=member_mapping
        )

        # Build response data
        mapping_data = {
            'mapping_definition': {
                'mapping_id': mapping_def.mapping_id,
                'code': mapping_def.code,
                'name': mapping_def.name,
            },
            'variable_mapping': {
                'variable_mapping_id': variable_mapping.variable_mapping_id,
                'code': variable_mapping.code,
                'name': variable_mapping.name,
                'items': []
            },
            'member_mapping': {
                'member_mapping_id': member_mapping.member_mapping_id,
                'code': member_mapping.code,
                'name': member_mapping.name,
                'items': []
            }
        }
        # Add variable mapping items
        for item in variable_mapping_items:
            mapping_data['variable_mapping']['items'].append({
                'source_variable': {
                    'variable_id': item.variable_id.variable_id,
                    'code': item.variable_id.code,
                    'name': item.variable_id.name
                },
                'target_variable': {
                    'variable_id': item.variable_id.variable_id,
                    'code': item.variable_mapping_id.code,
                    'name': item.variable_mapping_id.name
                }
            })

        # Add member mapping items
        for item in member_mapping_items:
            mapping_data['member_mapping']['items'].append({
                'member_mapping_row': item.member_mapping_row,
                'variable': {
                    'variable_id': item.variable_id.variable_id,
                    'code': item.variable_id.code,
                    'name': item.variable_id.name
                },
                'member': {
                    'member_id': item.member_id.member_id,
                    'code': item.member_id.code,
                    'name': item.member_id.name
                },
                'is_source': item.is_source
            })
        logger.info("Successfully retrieved mapping details")
        return JsonResponse({
            'status': 'success',
            'data': mapping_data
        })

    except MAPPING_DEFINITION.DoesNotExist:
        logger.error(f"Mapping {mapping_id} not found")
        return JsonResponse({
            'status': 'error',
            'message': f'Mapping {mapping_id} not found'
        })
    except Exception as e:
        logger.error(f"Error getting mapping details: {str(e)}", exc_info=True)
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        })
