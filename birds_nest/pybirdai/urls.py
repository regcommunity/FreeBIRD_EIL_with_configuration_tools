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
from django.urls import path

from . import views
from . import report_views

from django.views.generic import TemplateView
from .views import JoinIdentifierListView, DuplicatePrimaryMemberIdListView

app_name = 'pybirdai'  # Add this line if using namespaces

urlpatterns = [
    path('', views.home_view, name='home'),  # This should handle the root URL of your app
    path('run_import_input_model_from_sqldev/', views.run_import_input_model_from_sqldev, name='run_import_input_model_from_sqldev'),
    path('edit-variable-mappings/', views.edit_variable_mappings, name='edit_variable_mappings'),
    path('create-variable-mapping/', views.create_variable_mapping, name='create_variable_mapping'),
    path('delete-variable-mapping/<str:variable_mapping_id>/', views.delete_variable_mapping, name='delete_variable_mapping'),
    path('edit-variable-mapping-items/', views.edit_variable_mapping_items, name='edit_variable_mapping_items'),
    path('create-variable-mapping-item/', views.create_variable_mapping_item, name='create_variable_mapping_item'),
    path('delete-variable-mapping-item/', views.delete_variable_mapping_item, name='delete_variable_mapping_item'),
    path('review-semantic-integrations/', report_views.review_semantic_integrations, name='review_semantic_integrations'),
    path('review-filters/', report_views.review_filters, name='review_filters'),
    path('review-import-hierarchies/', report_views.review_import_hierarchies, name='review_import_hierarchies'),
    path('review-report-templates/', report_views.review_report_templates, name='review_report_templates'),
    path('edit-member-mappings/', views.edit_member_mappings, name='edit_member_mappings'),
    path('delete-member-mapping/<str:member_mapping_id>/', views.delete_member_mapping, name='delete_member_mapping'),
    path('edit-member-mapping-items/', views.edit_member_mapping_items, name='edit_member_mapping_items'),
    path('delete-member-mapping-item/<int:item_id>/', views.delete_member_mapping_item, name='delete_member_mapping_item'),
    path('edit-cube-links/', views.edit_cube_links, name='edit_cube_links'),
    path('delete-cube-link/<str:cube_link_id>/', views.delete_cube_link, name='delete_cube_link'),
    path('add-cube-link/', views.add_cube_link, name='add_cube_link'),
    path('edit-cube-structure-item-links/', views.edit_cube_structure_item_links, name='edit_cube_structure_item_links'),
    path('delete-cube-structure-item-link/<str:cube_structure_item_link_id>/', views.delete_cube_structure_item_link, name='delete_cube_structure_item_link'),
    path('edit-mapping-to-cubes/', views.edit_mapping_to_cubes, name='edit_mapping_to_cubes'),
    path('create-mapping-to-cube/', views.create_mapping_to_cube, name='create_mapping_to_cube'),
    path('delete-mapping-to-cube/<int:mapping_to_cube_id>/', views.delete_mapping_to_cube, name='delete_mapping_to_cube'),
    path('edit-mapping-definitions/', views.edit_mapping_definitions, name='edit_mapping_definitions'),
    path('create-mapping-definition/', views.create_mapping_definition, name='create_mapping_definition'),
    path('delete-mapping-definition/<str:mapping_id>/', views.delete_mapping_definition, name='delete_mapping_definition'),
    path('delete-cube/<str:cube_id>/', views.delete_cube, name='delete_cube'),
    path('import_report_templates/', views.import_report_templates, name='import_report_templates'),
    path('run_import_semantic_integrations_from_website/', views.run_import_semantic_integrations_from_website, name='run_import_semantic_integrations_from_website'),
    path('run_import_hierarchies/', views.run_import_hierarchies, name='run_import_hierarchies'),
    path('missing-children/', report_views.missing_children, name='missing_children'),
    path('missing-members/', report_views.missing_members, name='missing_members'),
    path('mappings-missing-members/', report_views.mappings_missing_members, name='mappings_missing_members'),
    path('mappings-missing-variables/', report_views.mappings_missing_variables, name='mappings_missing_variables'),
    path('mappings-warnings-summary/', report_views.mappings_warnings_summary, name='mappings_warnings_summary'),
    path('run-create-output-concepts/', views.run_create_filters, name='run_create_filters'),
    path('run-create-transformation-meta-data/', views.run_create_joins_meta_data, name='run_create_joins_meta_data'),
    path('review-transformation-meta-data/', report_views.review_join_meta_data, name='review_join_meta_data'),
    path('run-delete-transformation-meta-data/', views.run_delete_joins_meta_data, name='run_delete_joins_meta_data'),
    path('run_create_joins_meta_data/', views.run_create_joins_meta_data, name='run_create_joins_meta_data'),
    path('run-create-python-transformations/', views.run_create_python_joins, name='run_create_python_joins'),
    path('executable-transformations/', report_views.executable_transformations, name='executable_transformations'),
    path('create-input-structures/', report_views.input_model, name='input_model'),
    path('create-transformation-rules-in-python/', report_views.create_transformation_rules_in_python, name='create_transformation_rules_in_python'),
    path('create-transformation-rules-in-smcubes/', report_views.create_transformation_rules_in_smcubes, name='create_transformation_rules_in_smcubes'),
    path('run-create-executable-filters/', views.run_create_executable_filters, name='run_create_executable_filters'),
    path('run-create-executable-filters-from-db/', views.run_create_executable_filters_from_db, name='run_create_executable_filters_from_db'),
    path('run-create-python-joins-from-db/', views.run_create_python_joins_from_db, name='run_create_python_joins_from_db'),
    path('execute-data-point/<str:data_point_id>/', views.execute_data_point, name='execute_data_point'),
    path('show-report/<str:report_id>/', views.show_report, name='show_report'),
    path('report-templates/', report_views.report_templates, name='report_templates'),
    path('lineage/', views.list_lineage_files, name='list_lineage_files'),
    path('lineage/<str:filename>/', views.view_csv_file, name='view_csv'),
    path('upload-sqldev-eil-files/', views.upload_sqldev_eil_files, name='upload_sqldev_eil_files'),
    path('upload-technical-export-files/', views.upload_technical_export_files, name='upload_technical_export_files'),
    path('create-bird-database/', report_views.create_bird_database, name='create_bird_database'),
    path('import-data-model-artefacts/', report_views.import_data_model_artefacts, name='import_data_model_artefacts'),
    path('import-sqldev-eil-files/', report_views.import_sqldev_eil_files, name='import_sqldev_eil_files'),
    path('import-sqldev-eldm-files/', report_views.import_sqldev_eldm_files, name='import_sqldev_eldm_files'),
    path('import-bird-eil-datamodel/', report_views.import_bird_eil_datamodel, name='import_bird_eil_datamodel'),
    path('import-bird-eldm-datamodel/', report_views.import_bird_eldm_datamodel, name='import_bird_eldm_datamodel'),
    path('create-django-models/', views.create_django_models, name='create_django_models'),
    path('create-database-manual-steps/', report_views.create_database_manual_steps, name='create_database_manual_steps'),
    path('populate-bird-metadata-database/', report_views.populate_bird_metadata_database, name='populate_bird_metadata_database'),
    path('import-report-template-instructions/', report_views.import_report_template_instructions, name='import_report_template_instructions'),
    path('delete-existing-contents-of-bird-metadata-database/', views.delete_existing_contents_of_bird_metadata_database, name='delete_existing_contents_of_bird_metadata_database'),
    path('create-transformations-metadata/', report_views.create_transformations_metadata, name='create_transformations_metadata'),
    path('create-transformation-rules-configuration/', report_views.create_transformation_rules_configuration, name='create_transformation_rules_configuration'),
    path('derivation-transformation-rules/', report_views.derivation_transformation_rules, name='derivation_transformation_rules'),
    path('manual-edits/', report_views.manual_edits, name='manual_edits'),
    path('upload-joins-configuration/', views.upload_joins_configuration, name='upload_joins_configuration'),
    path('insert-data-into-bird-database/', report_views.insert_data_into_bird_database, name='insert_data_into_bird_database'),
    path('combinations/', views.combinations, name='combinations'),
    path('combination-items/', views.combination_items, name='combination_items'),
    path('output-layers/', views.output_layers, name='output_layers'),
    path('delete-combination/<str:combination_id>/', views.delete_combination, name='delete_combination'),
    path('delete-combination-item/<int:item_id>/', views.delete_combination_item, name='delete_combination_item'),
    path('join-identifiers/', JoinIdentifierListView.as_view(), name='join_identifier_list'),
    path('duplicate-primary-member-ids/', views.duplicate_primary_member_id_list, name='duplicate_primary_member_id_list'),
    path('add-cube-structure-item-link/', views.add_cube_structure_item_link, name='add_cube_structure_item_link'),
    path('upload_sqldev_eldm_files/', views.upload_sqldev_eldm_files, name='upload_sqldev_eldm_files'),
    path('show-gaps/', views.show_gaps, name='show_gaps'),
    path('create_member_mapping/', views.create_member_mapping, name='create_member_mapping'),
    path('edit_member_mapping_items/', views.edit_member_mapping_items, name='edit_member_mapping_items'),
    path('add_member_mapping_item/', views.add_member_mapping_item, name='add_member_mapping_item'),
    path('view_member_mapping_items_by_row/', views.view_member_mapping_items_by_row, name='view_member_mapping_items_by_row'),
    path('export-database-to-csv/', views.export_database_to_csv, name='export_database_to_csv'),
    path('bird_diffs_and_corrections/', views.bird_diffs_and_corrections, name='bird_diffs_and_corrections'),
    path('convert_ldm_to_sdd_hierarchies/', views.convert_ldm_to_sdd_hierarchies, name='convert_ldm_to_sdd_hierarchies'),
    path('view_ldm_to_sdd_results/', views.view_ldm_to_sdd_results, name='view_ldm_to_sdd_results'),
    path('import_members_from_csv/', views.import_members_from_csv, name='import_members_from_csv'),
    path('import_variables_from_csv/', views.import_variables_from_csv, name='import_variables_from_csv'),
    path('return_semantic_integration_menu/', views.return_semantic_integration_menu, name='return_semantic_integration_menu'),
    path('edit_mapping_endpoint/', views.edit_mapping_endpoint, name='edit_mapping_endpoint'),
    path('add_variable_endpoint/', views.add_variable_endpoint, name='add_variable_endpoint'),
    path('get_domain_members/<str:variable_id>/', views.get_domain_members, name='get_domain_members'),
    path('get_mapping_details/<str:mapping_id>/', views.get_mapping_details, name='get_mapping_details'),


]
