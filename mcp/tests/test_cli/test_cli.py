import pytest
import json
from pathlib import Path
from click.testing import CliRunner
from mcp.cli import cli

@pytest.fixture
def runner():
    return CliRunner()

@pytest.fixture
def sample_context(tmp_path):
    context = {
        "version": "v1",
        "project": {
            "name": "test-project",
            "type": "web",
            "language": "python"
        },
        "user": {
            "role": "developer",
            "expertise": "intermediate"
        },
        "current_state": {
            "code": "print('Hello, World!')",
            "cursor_position": 0,
            "selection": None
        }
    }
    context_file = tmp_path / "context.json"
    with open(context_file, 'w') as f:
        json.dump(context, f)
    return context_file

@pytest.fixture
def sample_updates(tmp_path):
    updates = {
        "project": {
            "name": "updated-project"
        },
        "user": {
            "expertise": "advanced"
        }
    }
    updates_file = tmp_path / "updates.json"
    with open(updates_file, 'w') as f:
        json.dump(updates, f)
    return updates_file

def test_list_schemas(runner):
    result = runner.invoke(cli, ['list-schemas', 'coding'])
    assert result.exit_code == 0
    assert "Available versions for coding:" in result.output

def test_convert_context(runner, sample_context):
    result = runner.invoke(cli, [
        'convert-context',
        str(sample_context),
        'coding',
        '--version', 'v1'
    ])
    assert result.exit_code == 0
    assert "test-project" in result.output
    assert "web" in result.output
    assert "python" in result.output

def test_create_context(runner):
    result = runner.invoke(cli, [
        'create-context',
        'coding',
        '--version', 'v1'
    ])
    assert result.exit_code == 0
    context = json.loads(result.output)
    assert context["project"]["name"] == "new-project"
    assert context["project"]["type"] == "web"
    assert context["project"]["language"] == "python"

def test_validate_context(runner, sample_context):
    result = runner.invoke(cli, [
        'validate-context',
        str(sample_context),
        'coding',
        '--version', 'v1'
    ])
    assert result.exit_code == 0
    assert "Context is valid!" in result.output

def test_update_context(runner, sample_context, sample_updates):
    result = runner.invoke(cli, [
        'update-context',
        str(sample_context),
        str(sample_updates),
        'coding',
        '--version', 'v1'
    ])
    assert result.exit_code == 0
    updated = json.loads(result.output)
    assert updated["project"]["name"] == "updated-project"
    assert updated["user"]["expertise"] == "advanced"
    assert updated["project"]["type"] == "web"  # Original value preserved

def test_invalid_context(runner, tmp_path):
    invalid_context = {
        "version": "v1",
        "project": {
            "name": "test-project"
            # Missing required fields
        }
    }
    context_file = tmp_path / "invalid_context.json"
    with open(context_file, 'w') as f:
        json.dump(invalid_context, f)
    
    result = runner.invoke(cli, [
        'validate-context',
        str(context_file),
        'coding',
        '--version', 'v1'
    ])
    assert result.exit_code != 0
    assert "Error:" in result.output

def test_output_file(runner, sample_context, tmp_path):
    output_file = tmp_path / "output.txt"
    result = runner.invoke(cli, [
        'convert-context',
        str(sample_context),
        'coding',
        '--version', 'v1',
        '--output', str(output_file)
    ])
    assert result.exit_code == 0
    assert output_file.exists()
    with open(output_file, 'r') as f:
        content = f.read()
        assert "test-project" in content
        assert "web" in content
        assert "python" in content 