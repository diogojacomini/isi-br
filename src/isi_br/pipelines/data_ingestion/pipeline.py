"""
This is a boilerplate pipeline 'data_ingestion'
generated using Kedro 0.19.13
"""
from .nodes import extract_transform_html_table
from kedro.pipeline import node, Pipeline, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=extract_transform_html_table,
            inputs=['params:columns_mapping'],
            outputs="tb_cds",
            name="extract_transform_html_table_node"
        ),
    ])
