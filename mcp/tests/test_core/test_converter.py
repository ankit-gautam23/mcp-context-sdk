import pytest
from mcp.core.converter import ContextConverter, PromptTemplate
from pathlib import Path

@pytest.fixture
def converter():
    schema_path = Path(__file__).parent.parent.parent / "schemas" / "coding" / "v1" / "context.json"
    return ContextConverter(str(schema_path))

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

def test_converter_initialization(converter):
    """Test converter initialization."""
    assert converter.schema is not None
    assert "properties" in converter.schema

def test_validate_context(converter, sample_context):
    """Test context validation."""
    assert converter.validate_context(sample_context) is True

def test_invalid_context(converter):
    """Test invalid context validation."""
    invalid_context = {
        "version": "v1.0.0",
        "project": {
            "name": "test-project"
            # Missing required fields
        }
    }
    with pytest.raises(ValueError):
        converter.validate_context(invalid_context)

def test_to_prompt(converter, sample_context):
    """Test context to prompt conversion."""
    prompt = converter.to_prompt(sample_context)
    assert isinstance(prompt, str)
    assert "test-project" in prompt
    assert "python" in prompt
    assert "developer" in prompt

def test_custom_template(converter, sample_context):
    """Test custom template usage."""
    template = "Project: {{project.name}}\nLanguage: {{project.language}}"
    prompt = converter.to_prompt(sample_context, template)
    assert "Project: test-project" in prompt
    assert "Language: python" in prompt

def test_prompt_template():
    """Test prompt template management."""
    template_manager = PromptTemplate()
    
    # Add template
    template_manager.add_template("test", "Hello {{name}}")
    
    # Get template
    template = template_manager.get_template("test")
    assert template == "Hello {{name}}"
    
    # List templates
    templates = template_manager.list_templates()
    assert "test" in templates
    
    # Test non-existent template
    with pytest.raises(KeyError):
        template_manager.get_template("nonexistent")

def test_flatten_dict(converter, sample_context):
    """Test dictionary flattening."""
    flattened = converter._flatten_dict(sample_context)
    assert "project.name" in flattened
    assert "user.role" in flattened
    assert flattened["project.name"] == "test-project"
    assert flattened["user.role"] == "developer" 