import pytest
from mcp.core.context import ContextBuilder
from mcp.core.schema import SchemaLoader

def test_context_builder_initialization():
    builder = ContextBuilder()
    assert builder is not None

def test_schema_loading():
    loader = SchemaLoader()
    schemas = loader.list_available_schemas()
    assert isinstance(schemas, list)
    assert len(schemas) > 0

def test_context_validation():
    builder = ContextBuilder()
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name"]
    }
    context = {"name": "Test User", "age": 25}
    assert builder.validate_context(context, schema) is True

def test_invalid_context():
    builder = ContextBuilder()
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"}
        },
        "required": ["name"]
    }
    context = {"age": "not_an_integer"}
    with pytest.raises(ValueError):
        builder.validate_context(context, schema) 