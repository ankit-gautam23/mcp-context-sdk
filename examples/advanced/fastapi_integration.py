"""Advanced example showing FastAPI integration with MCP SDK."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from mcp_context_sdk.core.context import ContextBuilder
from mcp_context_sdk.integrations.fastapi import FastAPIContextMiddleware

app = FastAPI(title="MCP SDK FastAPI Example")

# Add MCP context middleware
app.add_middleware(FastAPIContextMiddleware)

class CodeRequest(BaseModel):
    """Request model for code generation."""
    language: str
    task_type: str
    complexity: str
    requirements: Optional[List[str]] = None
    dependencies: Optional[List[str]] = None

@app.post("/generate-code")
async def generate_code(request: CodeRequest):
    """Generate code based on the provided context."""
    try:
        # Create context using the request data
        context = ContextBuilder()\
            .with_schema("coding")\
            .with_version("v1")\
            .with_property("language", request.language)\
            .with_property("task_type", request.task_type)\
            .with_property("complexity", request.complexity)\
            .with_property("context", {
                "requirements": request.requirements or [],
                "dependencies": request.dependencies or []
            })\
            .build()

        # Here you would typically use the context with an AI model
        # For this example, we'll just return the context
        return {
            "status": "success",
            "context": context.to_dict(),
            "message": "Context created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 