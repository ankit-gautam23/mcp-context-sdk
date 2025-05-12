import pytest
from mcp.schemas.loader import SchemaLoader, SchemaRegistry
from pathlib import Path
import json
import os

@pytest.fixture
def schema_dir(tmp_path):
    """Create a temporary schema directory structure."""
    # Create coding/v1 schema
    coding_v1_dir = tmp_path / "coding" / "v1"
    coding_v1_dir.mkdir(parents=True)
    
    coding_v1_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Coding Context Schema v1",
        "type": "object",
        "required": ["version", "project"],
        "properties": {
            "version": {
                "type": "string",
                "pattern": "^v\\d+\\.\\d+\\.\\d+$"
            },
            "project": {
                "type": "object",
                "required": ["name", "type", "language"],
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "language": {"type": "string"}
                }
            }
        }
    }
    
    with open(coding_v1_dir / "context.json", "w") as f:
        json.dump(coding_v1_schema, f)
    
    return tmp_path

@pytest.fixture
def schema_loader(schema_dir):
    return SchemaLoader(str(schema_dir))

@pytest.fixture
def schema_registry():
    return SchemaRegistry()

def test_schema_loader_initialization(schema_loader):
    """Test schema loader initialization."""
    assert schema_loader.schema_dir is not None
    assert len(schema_loader.schemas) > 0

def test_get_schema(schema_loader):
    """Test getting a schema by domain and version."""
    schema = schema_loader.get_schema("coding", "v1")
    assert schema is not None
    assert schema["title"] == "Coding Context Schema v1"
    assert "properties" in schema

def test_get_latest_schema(schema_loader):
    """Test getting the latest schema version."""
    schema = schema_loader.get_schema("coding")
    assert schema is not None
    assert schema["title"] == "Coding Context Schema v1"

def test_list_domains(schema_loader):
    """Test listing available schema domains."""
    domains = schema_loader.list_domains()
    assert "coding" in domains

def test_list_versions(schema_loader):
    """Test listing available schema versions."""
    versions = schema_loader.list_versions("coding")
    assert "v1" in versions

def test_validate_context(schema_loader):
    """Test context validation against schema."""
    context = {
        "version": "v1.0.0",
        "project": {
            "name": "test-project",
            "type": "web",
            "language": "python"
        }
    }
    assert schema_loader.validate_context(context, "coding", "v1") is True

def test_invalid_context(schema_loader):
    """Test validation of invalid context."""
    invalid_context = {
        "version": "v1.0.0",
        "project": {
            "name": "test-project"
            # Missing required fields
        }
    }
    with pytest.raises(ValueError):
        schema_loader.validate_context(invalid_context, "coding", "v1")

def test_get_schema_metadata(schema_loader):
    """Test getting schema metadata."""
    metadata = schema_loader.get_schema_metadata("coding", "v1")
    assert metadata["title"] == "Coding Context Schema v1"
    assert "required_fields" in metadata
    assert "properties" in metadata

def test_schema_registry_initialization(schema_registry):
    """Test schema registry initialization."""
    assert schema_registry.registry == {}

def test_register_schema(schema_registry):
    """Test registering a schema."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "test": {"type": "string"}
        }
    }
    
    schema_registry.register_schema("test", "v1", schema)
    assert "test.v1" in schema_registry.registry

def test_invalid_schema_registration(schema_registry):
    """Test registering an invalid schema."""
    invalid_schema = {
        "type": "object"
        # Missing required fields
    }
    
    with pytest.raises(ValueError):
        schema_registry.register_schema("test", "v1", invalid_schema)

def test_get_registered_schema(schema_registry):
    """Test getting a registered schema."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "test": {"type": "string"}
        }
    }
    
    schema_registry.register_schema("test", "v1", schema)
    retrieved = schema_registry.get_schema("test", "v1")
    assert retrieved == schema

def test_list_registered_schemas(schema_registry):
    """Test listing registered schemas."""
    schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "test": {"type": "string"}
        }
    }
    
    schema_registry.register_schema("test", "v1", schema)
    schemas = schema_registry.list_registered_schemas()
    assert len(schemas) == 1
    assert schemas[0]["key"] == "test.v1" 