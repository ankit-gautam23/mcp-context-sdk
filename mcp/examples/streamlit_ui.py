import streamlit as st
from mcp.core.builder import ContextBuilder
from mcp.core.converter import ContextConverter
from mcp.schemas.loader import SchemaLoader

# Initialize MCP components
schema_loader = SchemaLoader()
context_builder = ContextBuilder(schema_loader)
converter = ContextConverter()

st.title("MCP Context Editor")

# Project settings
st.sidebar.header("Project Settings")
project_name = st.sidebar.text_input("Project Name", "my-project")
project_type = st.sidebar.selectbox(
    "Project Type",
    ["web", "mobile", "desktop", "library", "api", "other"]
)
language = st.sidebar.text_input("Language", "python")

# User settings
st.sidebar.header("User Settings")
user_role = st.sidebar.selectbox(
    "Role",
    ["developer", "student", "researcher", "other"]
)
expertise_level = st.sidebar.selectbox(
    "Expertise Level",
    ["beginner", "intermediate", "advanced", "expert"]
)

# Main content
st.header("Code Editor")
code = st.text_area("Enter your code", height=300)

if st.button("Generate Context"):
    # Build context
    context = context_builder.build_coding_context(
        project_name=project_name,
        project_type=project_type,
        language=language,
        file_content=code,
        user_role=user_role,
        expertise_level=expertise_level
    )
    
    # Convert to prompt
    prompt = converter.to_prompt(context)
    
    # Display context
    st.header("Generated Context")
    st.json(context)
    
    # Display prompt
    st.header("Generated Prompt")
    st.write(prompt) 