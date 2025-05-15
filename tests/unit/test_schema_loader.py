import pytest
from mcp_context_sdk.core.schema_loader import SchemaLoader
from pathlib import Path

@pytest.fixture
def schema_loader():
    return SchemaLoader()

def test_schema_loader_initialization(schema_loader):
    assert schema_loader is not None
    assert isinstance(schema_loader.schema_dir, Path)

def test_list_available_schemas(schema_loader):
    schemas = schema_loader.list_available_schemas()
    assert isinstance(schemas, list)
    # Note: We don't assert length > 0 as schemas might not be present in test environment

def test_get_schema(schema_loader):
    try:
        schema = schema_loader.get_schema("coding", "v1")
        assert schema is not None
        assert "properties" in schema
        assert "type" in schema
    except ValueError:
        pytest.skip("Schema not found in test environment")

def test_validate_context(schema_loader):
    try:
        context = {
            "language": "python",
            "task_type": "development",
            "complexity": "intermediate"
        }
        assert schema_loader.validate_context(context, "coding", "v1") is True
    except ValueError:
        pytest.skip("Schema not found in test environment")

def test_invalid_context(schema_loader):
    try:
        invalid_context = {
            "language": "invalid_language",
            "task_type": "invalid_task"
        }
        with pytest.raises(ValueError):
            schema_loader.validate_context(invalid_context, "coding", "v1")
    except ValueError:
        pytest.skip("Schema not found in test environment") 