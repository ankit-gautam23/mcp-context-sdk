import click
from mcp.core.builder import ContextBuilder
from mcp.core.converter import ContextConverter
from mcp.schemas.loader import SchemaLoader

@click.command()
@click.argument('project_name')
@click.argument('project_type')
@click.argument('language')
@click.argument('file_content')
@click.option('--user_role', default='developer', help='User role')
@click.option('--expertise_level', default='intermediate', help='Expertise level')
def generate_prompt(project_name, project_type, language, file_content, user_role, expertise_level):
    """Generate a prompt from context."""
    # Initialize MCP components
    schema_loader = SchemaLoader()
    context_builder = ContextBuilder(schema_loader)
    converter = ContextConverter()

    # Build context
    context = context_builder.build_coding_context(
        project_name=project_name,
        project_type=project_type,
        language=language,
        file_content=file_content,
        user_role=user_role,
        expertise_level=expertise_level
    )

    # Convert to prompt
    prompt = converter.to_prompt(context)

    # Output prompt
    click.echo(prompt)

if __name__ == '__main__':
    generate_prompt() 