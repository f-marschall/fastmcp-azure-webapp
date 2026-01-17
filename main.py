import math
from fastmcp import FastMCP

mcp = FastMCP("MCP test server 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def greet(name: str) -> str:
    """Greet a person by name"""
    return f"Hello, {name}!"

@mcp.prompt
def welcome_message() -> str:
    return "Welcome to the MCP test server! How can I assist you today?"

@mcp.resource("resources://pi_value")
def pi_value() -> float:
    return math.pi

# For ASGI deployment (Uvicorn/Gunicorn)
app = mcp.http_app()

# For Azure Web App compatibility (looks for 'application')
application = app

# For local development
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)