import pytest
from mcp_context_sdk.core.schema_loader import SchemaLoader

def test_schema_loader_initialization():
    loader = SchemaLoader()
    assert loader is not None
    assert loader.schema_dir.exists()

def test_list_available_schemas():
    loader = SchemaLoader()
    schemas = loader.list_available_schemas()
    assert isinstance(schemas, list)
    assert len(schemas) > 0

def test_get_schema():
    loader = SchemaLoader()
    schema = loader.get_schema("coding", "v1")
    assert schema is not None
    assert "properties" in schema
    assert "type" in schema

def test_validate_context():
    loader = SchemaLoader()
    context = {
        "language": "python",
        "task_type": "development",
        "complexity": "intermediate"
    }
    assert loader.validate_context(context, "coding", "v1") is True

def test_invalid_context():
    loader = SchemaLoader()
    invalid_context = {
        "language": "invalid_language",
        "task_type": "invalid_task"
    }
    with pytest.raises(ValueError):
        loader.validate_context(invalid_context, "coding", "v1") 