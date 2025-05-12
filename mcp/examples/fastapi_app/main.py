from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent.parent))

from mcp.core.builder import ContextBuilder
from mcp.core.converter import ContextConverter
from mcp.schemas.loader import SchemaLoader
from mcp.integrations.fastapi import (
    create_mcp_app,
    MCPEndpoint,
    MCPRequest,
    MCPResponse
)

# Initialize MCP components
schema_loader = SchemaLoader()
context_builder = ContextBuilder(schema_loader)
converter = ContextConverter()

# Create FastAPI app with MCP
app = create_mcp_app(
    context_builder=context_builder,
    domain="coding",
    version="v1"
)

# Create MCP endpoint decorator
mcp_endpoint = MCPEndpoint(
    context_builder=context_builder,
    domain="coding",
    version="v1"
)

class CodeRequest(MCPRequest):
    """Request model for code processing."""
    code: str

@app.post("/process-code")
@mcp_endpoint
async def process_code(request: Request, context: dict):
    """Process code with MCP context."""
    try:
        body = await request.json()
        code_request = CodeRequest(**body)
        
        # Convert context to prompt
        prompt = converter.to_prompt(context)
        
        # Process code (example)
        result = {
            "status": "success",
            "message": "Code processed successfully",
            "context": prompt
        }
        
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/context-info")
@mcp_endpoint
async def get_context_info(request: Request, context: dict):
    """Get information about the current context."""
    return {
        "schema_version": context.get("version"),
        "project": context.get("project"),
        "user": context.get("user")
    }

@app.post("/update-context")
@mcp_endpoint
async def update_context(request: Request, context: dict):
    """Update the current context."""
    try:
        updates = await request.json()
        updated_context = context_builder.update_context(
            context=context,
            updates=updates,
            domain="coding",
            version="v1"
        )
        return updated_context
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 