import pytest
from mcp.core.builder import ContextBuilder
from mcp.schemas.loader import SchemaLoader
from pathlib import Path
import json
import os

@pytest.fixture
def schema_loader():
    return SchemaLoader()

@pytest.fixture
def builder(schema_loader):
    return ContextBuilder(schema_loader)

@pytest.fixture
def sample_context():
    return {
        "version": "v1.0.0",
        "project": {
            "name": "test-project",
            "type": "web",
            "language": "python"
        },
        "user": {
            "role": "developer",
            "expertise_level": "intermediate"
        },
        "current_state": {
            "file": {
                "path": "test.py",
                "content": "print('hello')",
                "language": "python"
            },
            "cursor_position": {
                "line": 1,
                "column": 1
            }
        }
    }

def test_builder_initialization(builder):
    """Test builder initialization."""
    assert builder.schema_loader is not None
    assert builder.converter is not None

def test_build_coding_context(builder):
    """Test building coding context."""
    context = builder.build_coding_context(
        project_name="test-project",
        project_type="web",
        language="python",
        file_path="test.py",
        file_content="print('hello')",
        cursor_line=1,
        cursor_column=1
    )
    
    assert context["version"] == "v1.0.0"
    assert context["project"]["name"] == "test-project"
    assert context["project"]["type"] == "web"
    assert context["project"]["language"] == "python"
    assert context["current_state"]["file"]["path"] == "test.py"
    assert context["current_state"]["file"]["content"] == "print('hello')"
    assert context["current_state"]["cursor_position"]["line"] == 1
    assert context["current_state"]["cursor_position"]["column"] == 1

def test_build_coding_context_defaults(builder):
    """Test building coding context with defaults."""
    context = builder.build_coding_context(
        project_name="test-project",
        project_type="web",
        language="python"
    )
    
    assert context["version"] == "v1.0.0"
    assert context["project"]["name"] == "test-project"
    assert context["current_state"]["file"]["path"] == ""
    assert context["current_state"]["file"]["content"] == ""
    assert context["current_state"]["cursor_position"]["line"] == 1
    assert context["current_state"]["cursor_position"]["column"] == 1

def test_build_from_file(builder, tmp_path):
    """Test building context from file."""
    # Create temporary context file
    context_file = tmp_path / "context.json"
    context_data = {
        "version": "v1.0.0",
        "project": {
            "name": "test-project",
            "type": "web",
            "language": "python"
        },
        "user": {
            "role": "developer",
            "expertise_level": "intermediate"
        }
    }
    context_file.write_text(json.dumps(context_data))
    
    # Build context from file
    context = builder.build_from_file(str(context_file), "coding", "v1")
    assert context["project"]["name"] == "test-project"
    assert context["project"]["type"] == "web"

def test_fill_defaults(builder):
    """Test filling defaults in context."""
    context = {
        "version": "v1.0.0",
        "project": {
            "name": "test-project"
        }
    }
    
    schema = builder.schema_loader.get_schema("coding", "v1")
    builder._fill_defaults(context, schema)
    
    assert "user" in context
    assert "current_state" in context
    assert context["user"]["role"] == "developer"
    assert context["user"]["expertise_level"] == "intermediate"

def test_update_context(builder, sample_context):
    """Test updating context."""
    updates = {
        "project": {
            "name": "updated-project",
            "framework": "django"
        }
    }
    
    updated = builder.update_context(
        context=sample_context,
        updates=updates,
        domain="coding",
        version="v1"
    )
    
    assert updated["project"]["name"] == "updated-project"
    assert updated["project"]["framework"] == "django"
    assert updated["project"]["type"] == "web"  # Original value preserved
    assert len(updated["context_history"]) > len(sample_context["context_history"])

def test_deep_merge(builder):
    """Test deep merging of dictionaries."""
    dict1 = {
        "a": 1,
        "b": {
            "c": 2,
            "d": 3
        }
    }
    dict2 = {
        "b": {
            "c": 4,
            "e": 5
        },
        "f": 6
    }
    
    merged = builder._deep_merge(dict1, dict2)
    assert merged["a"] == 1
    assert merged["b"]["c"] == 4
    assert merged["b"]["d"] == 3
    assert merged["b"]["e"] == 5
    assert merged["f"] == 6 