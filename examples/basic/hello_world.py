from mcp_context_sdk.core.schema_loader import SchemaLoader
from mcp_context_sdk.core.context import ContextBuilder

def main():
    # Initialize the schema loader
    loader = SchemaLoader()
    
    # Get available schemas
    schemas = loader.list_available_schemas()
    print(f"Available schemas: {schemas}")
    
    # Create a context builder
    builder = ContextBuilder()
    
    # Example context
    context = {
        "name": "Example Context",
        "version": "1.0.0"
    }
    
    print(f"Created context: {context}")

if __name__ == "__main__":
    main() 