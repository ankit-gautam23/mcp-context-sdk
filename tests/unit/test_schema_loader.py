import pytest
from mcp_context_sdk.core.schema_loader import SchemaLoader

def test_schema_loader_initialization():
    loader = SchemaLoader()
    assert loader is not None

def test_list_available_schemas():
    loader = SchemaLoader()
    schemas = loader.list_available_schemas()
    assert isinstance(schemas, list) 