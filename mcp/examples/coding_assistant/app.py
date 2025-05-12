import streamlit as st
from pathlib import Path
import sys
import os

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.core.builder import ContextBuilder
from mcp.core.converter import ContextConverter
from mcp.schemas.loader import SchemaLoader
from mcp.integrations.langchain import create_mcp_chain
from langchain.llms import OpenAI

# Initialize MCP components
schema_loader = SchemaLoader()
context_builder = ContextBuilder(schema_loader)
converter = ContextConverter()

# Initialize LangChain
llm = OpenAI(temperature=0.7)
chain = create_mcp_chain(
    llm=llm,
    context_builder=context_builder,
    domain="coding",
    version="v1"
)

def main():
    st.title("MCP Coding Assistant")
    
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
    
    if st.button("Get AI Assistance"):
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
        
        # Get AI response
        with st.spinner("Getting AI assistance..."):
            response = chain.run(query=prompt)
        
        # Display response
        st.header("AI Response")
        st.write(response)
        
        # Display context
        with st.expander("View MCP Context"):
            st.json(context)

if __name__ == "__main__":
    main() 