
import os
import django
from django.db import models
from django.conf import settings
import sys
import numpy as np

class DjangoSetup:
    @staticmethod
    def configure_django():
        """Configure Django settings without starting the application"""
        if not settings.configured:
            # Set up Django settings module for birds_nest in parent directory
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
            sys.path.insert(0, project_root)
            os.environ['DJANGO_SETTINGS_MODULE'] = 'birds_nest.settings'
            django.setup()

class DatabaseConnector:

    @staticmethod
    def get_cube_links_for_cube(cube_id):
        """Get all cube links that involve a specific cube (either as primary or foreign)"""
        DjangoSetup.configure_django()
        from pybirdai.bird_meta_data_model import CUBE_LINK
        return CUBE_LINK.objects.filter(
            models.Q(primary_cube_id=cube_id) |
            models.Q(foreign_cube_id=cube_id)
        ).select_related('primary_cube_id', 'foreign_cube_id')

    @staticmethod
    def get_all_cube_links():
        """Get cube structure item links for a specific cube link"""
        DjangoSetup.configure_django()
        from pybirdai.bird_meta_data_model import CUBE_LINK
        return CUBE_LINK.objects.all()

    @staticmethod
    def get_cube_structure_item_links(cube_link):
        """Get cube structure item links for a specific cube link"""
        DjangoSetup.configure_django()
        from pybirdai.bird_meta_data_model import CUBE_STRUCTURE_ITEM_LINK
        return CUBE_STRUCTURE_ITEM_LINK.objects.select_related(
            'primary_cube_variable_code',
            'foreign_cube_variable_code',
            'cube_link_id'
        ).filter(cube_link_id=cube_link)

    @classmethod
    def get_linked_cube_structure_items(cls, cube_link):
        """Get quadruples of linked cube structure items"""
        DjangoSetup.configure_django()
        from pybirdai.bird_meta_data_model import CUBE_STRUCTURE_ITEM_LINK

        linked_items = []
        structure_item_links = cls.get_cube_structure_item_links(cube_link)

        for link in structure_item_links:
            linked_items.append((
                link.cube_link_id.primary_cube_id,
                link.primary_cube_variable_code,
                link.cube_link_id.foreign_cube_id,
                link.foreign_cube_variable_code
            ))

        return linked_items

    @staticmethod
    def create_visualization_json(linked_cube_structure_items):
        """Create JSON structure for visualization"""
        nodes = {}
        edges = []

        for primary_cube, primary_item, foreign_cube, foreign_item in linked_cube_structure_items:
            # Add nodes
            if primary_cube.cube_id not in nodes:
                nodes[primary_cube.cube_id] = {
                    'id': primary_cube.cube_id,
                    'name': primary_cube.name,
                    'code': primary_cube.cube_id,
                    'items': [],
                    'is_source': True
                }
            nodes[primary_cube.cube_id]['items'].append({
                'code': primary_item.variable_id.variable_id,
                'name': primary_item.description
            })

            if foreign_cube.cube_id not in nodes:
                nodes[foreign_cube.cube_id] = {
                    'id': foreign_cube.cube_id,
                    'name': foreign_cube.name,
                    'code': foreign_cube.cube_id,
                    'items': [],
                    'is_source': False
                }
            nodes[foreign_cube.cube_id]['items'].append({
                'code': foreign_item.variable_id.variable_id,
                'name': foreign_item.description
            })

            # Add edges
            edges.append({
                'source': primary_cube.name,
                'target': foreign_cube.name,
                'sourceItem': primary_item.variable_id.variable_id,
                'targetItem': foreign_item.variable_id.variable_id,
                'linkType': "primary" # Default linkType since we no longer have link object
            })

        return {
            'nodes': list(nodes.values()),
            'edges': edges
        }

def return_line_break_at_23_char(string):
    if len(string) > 23:
        chunks = []
        for i in range(0, len(string), 23):
            chunks.append(string[i:i+23])
        return "\n".join(chunks)
    return string

class NetworkGraphGenerationService:
    @staticmethod
    def create_graph(json_data, file_name=""):
        """Create a Mermaid chart visualization from JSON data"""
        # Begin building the Mermaid flowchart definition
        mermaid_chart = "```mermaid\ngraph LR\n"  # Changed to TB (top to bottom)
        mermaid_chart += "    direction LR\n"     # Explicitly set direction

        # Organize nodes by type
        source_cubes = []
        source_items = []
        target_items = []
        target_cubes = []

        # Group nodes by type first
        for node in json_data['nodes']:
            is_source = node.get('is_source', any(edge['source'] == node['name'] for edge in json_data['edges']))
            node_id = "cube_" + ''.join(c if c.isalnum() else '_' for c in node['name'])

            if is_source:
                source_cubes.append((node_id, node))
                for item in node['items']:
                    item_id = f"{node_id}_{item['code']}"
                    source_items.append((item_id, item, node_id))
            else:
                target_cubes.append((node_id, node))
                for item in node['items']:
                    item_id = f"{node_id}_{item['code']}"
                    target_items.append((item_id, item, node_id))

        # Add source cubes and items in subgraphs
        for node_id, node in source_cubes:
            # Create a subgraph for each source cube with its items
            mermaid_chart += f"    subgraph {node_id}_group[\"{node['name']}\"]\n"
            mermaid_chart += f"        {node_id}((\"{return_line_break_at_23_char(node['name'])}\"));\n"

            # Add items that belong to this cube in the subgraph
            for item_id, item, parent_node_id in source_items:
                if parent_node_id == node_id:
                    mermaid_chart += f"        {item_id}[{item['code']}];\n"
                    # Connect source cube to source item
                    if f"        {node_id} --> {item_id};\n" not in mermaid_chart:
                        mermaid_chart += f"        {node_id} --> {item_id};\n"

            mermaid_chart += "    end\n"

        # Add target cubes and items in subgraphs
        for node_id, node in target_cubes:
            # Create a subgraph for each target cube with its items
            mermaid_chart += f"    subgraph {node_id}_group[\"{node['name']}\"];\n"
            mermaid_chart += f"        {node_id}((\"{return_line_break_at_23_char(node['name'])}\"));\n"

            # Add items that belong to this cube in the subgraph
            for item_id, item, parent_node_id in target_items:
                if parent_node_id == node_id:
                    mermaid_chart += f"        {item_id}{{{return_line_break_at_23_char(item['code'])}}};\n"
                    # Connect target item to target cube within the subgraph
                    if f"    {item_id} --> {node_id};\n" not in mermaid_chart:
                        mermaid_chart += f"        {item_id} --> {node_id};\n"

            mermaid_chart += "    end\n"

        # Connect target items to target cubes
        for item_id, item, node_id in target_items:
            if f"    {item_id} --> {node_id};\n" not in mermaid_chart:
                mermaid_chart += f"    {item_id} --> {node_id};\n"

        # Add cross connections between items
        for edge in json_data['edges']:
            source_id = "cube_" + ''.join(c if c.isalnum() else '_' for c in edge['source'])
            target_id = "cube_" + ''.join(c if c.isalnum() else '_' for c in edge['target'])

            source_item_id = f"{source_id}_{edge['sourceItem']}"
            target_item_id = f"{target_id}_{edge['targetItem']}"

            # Connect source item to target item with a dashed line
            if f"    {source_item_id} --- {target_item_id};\n" not in mermaid_chart:
                mermaid_chart += f"    {source_item_id} --- {target_item_id};\n"

        # Define colors
        source_cube_color = "#FF9933"
        target_cube_color = "#FFCC33"
        source_item_color = "#99CCFF"
        target_item_color = "#99FF99"

        # Add styling
        mermaid_chart += "    classDef sourceCube fill:#FF9933,stroke:#333,stroke-width:2px;\n"
        mermaid_chart += "    classDef targetCube fill:#FFCC33,stroke:#333,stroke-width:2px;\n"
        mermaid_chart += "    classDef sourceItem fill:#99CCFF,stroke:#333,stroke-width:1px;\n"
        mermaid_chart += "    classDef targetItem fill:#99FF99,stroke:#333,stroke-width:1px;\n"

        # Apply classes to nodes
        for node_id, node in source_cubes:
            mermaid_chart += f"    class {node_id} sourceCube;\n"

        for item_id, item, node_id in source_items:
            mermaid_chart += f"    class {item_id} sourceItem;\n"

        for item_id, item, node_id in target_items:
            mermaid_chart += f"    class {item_id} targetItem;\n"

        for node_id, node in target_cubes:
            mermaid_chart += f"    class {node_id} targetCube;\n"
            # Add legend as a subgraph

        mermaid_chart += """    subgraph Legend["Legend"]
        direction LR
        source_cube_legend[("Source Cube")]:::sourceCube
        source_item_legend["Source Item"]:::sourceItem
        target_item_legend{"Target Item"}:::targetItem
        target_cube_legend[("Target Cube")]:::targetCube

        source_cube_legend --> source_item_legend
        source_item_legend --- target_item_legend
        target_item_legend --> target_cube_legend

        class source_cube_legend sourceCube
        class source_item_legend sourceItem
        class target_item_legend targetItem
        class target_cube_legend targetCube
    end
    """

        # End Mermaid block
        mermaid_chart += "```\n\n"

        # Add a title section before the Mermaid chart
        title = f"# Mapping Visualization: {json_data['nodes'][1]['name']} to {json_data['nodes'][0]['name']}\n\n"

        # Complete markdown content
        markdown_content = mermaid_chart.replace("```mermaid","").replace("```","")

        html_content = f"""
        <!doctype html>
        <html lang="en">
          <body>
            <pre class="mermaid">
{markdown_content}
            </pre>
            <script type="module">
              import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
            </script>
          </body>
        </html>
        """

        # Save to file
        output_file = ""
        output_folder = "results/generated_linking_visualisations/"
        if file_name == "":
            output_file = f"{json_data['nodes'][1]['name']}_to_{json_data['nodes'][0]['name']}.html"
        else:
            output_file = file_name

        with open(output_folder+output_file, 'w') as f:
            f.write(html_content)

        return output_file


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualisation_service.py <cube_id>")
        sys.exit(1)

    # cube_id = sys.argv[1]

    links = DatabaseConnector.get_all_cube_links()
    cube_ids = [link.foreign_cube_id.cube_id for link in links]
    for cube_id in set(cube_ids):
        cube_links = DatabaseConnector.get_cube_links_for_cube(cube_id)
        json_list = []
        for cube_link in cube_links:
            linked_cube_structure_items = DatabaseConnector.get_linked_cube_structure_items(
                cube_link)
            json_list.append(DatabaseConnector.create_visualization_json(linked_cube_structure_items))

        # Merge all the JSONs
        merged_json = {'nodes': [], 'edges': []}
        for json_data in json_list:
            merged_json['nodes'].extend(json_data['nodes'])
            merged_json['edges'].extend(json_data['edges'])
        jason = merged_json
        file_path = NetworkGraphGenerationService.create_graph(jason, "")
