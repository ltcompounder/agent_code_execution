"""
MCP Client for Alpha Vantage Server
Handles connection and communication with the Alpha Vantage MCP server
"""

import os
import sys
import json
import asyncio
from pathlib import Path

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Warning: python-dotenv not installed. Using system environment variables.")

try:
    from mcp import ClientSession, StdioServerParameters
    from mcp.client.stdio import stdio_client
except ImportError:
    print("Error: MCP package not installed")
    print("Install with: pip install mcp")
    sys.exit(1)

# Get API key from environment
ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')

# Server configuration - using uvx to run av-mcp locally
SERVER_PARAMS = StdioServerParameters(
    command="uvx",
    args=["av-mcp", ALPHA_VANTAGE_API_KEY or ""],
    env=None
)


async def list_tools_async():
    """List all available tools from the Alpha Vantage MCP server."""
    if not ALPHA_VANTAGE_API_KEY:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set")
    
    if ALPHA_VANTAGE_API_KEY == "your-alpha-vantage-key-here":
        raise ValueError("Please replace placeholder with your actual Alpha Vantage API key in .env file")
    
    try:
        # Connect via stdio (local server run by uvx)
        async with stdio_client(SERVER_PARAMS) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                response = await session.list_tools()
                
                # Convert to list of dicts for easier handling
                tools = []
                for tool in response.tools:
                    tool_dict = {
                        "name": tool.name,
                        "description": tool.description,
                    }
                    if hasattr(tool, 'inputSchema'):
                        tool_dict["inputSchema"] = tool.inputSchema
                    tools.append(tool_dict)
                
                return tools
    except Exception as e:
        import traceback
        print(f"\nError connecting to Alpha Vantage MCP server:")
        print(f"Command: uvx av-mcp [API_KEY]")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print(f"\nMake sure:")
        print("  1. You have Python 3.13+ installed")
        print("  2. uv is installed: curl -LsSf https://astral.sh/uv/install.sh | sh")
        print("  3. Your API key is valid")
        print(f"\nFull traceback:")
        traceback.print_exc()
        raise


async def call_tool_async(tool_name: str, arguments: dict):
    """Call a specific MCP tool with given arguments."""
    if not ALPHA_VANTAGE_API_KEY:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set")
    
    try:
        # Connect via stdio (local server)
        async with stdio_client(SERVER_PARAMS) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                response = await session.call_tool(tool_name, arguments)
                
                # Extract content from response
                if hasattr(response, 'content'):
                    # MCP response has content array
                    results = []
                    for content in response.content:
                        if hasattr(content, 'text'):
                            results.append(content.text)
                        elif hasattr(content, 'data'):
                            results.append(content.data)
                    
                    if len(results) == 1:
                        # Try to parse as JSON if it's a string
                        if isinstance(results[0], str):
                            try:
                                return json.loads(results[0])
                            except json.JSONDecodeError:
                                return results[0]
                        return results[0]
                    return results
                
                return response
                
    except Exception as e:
        return {
            "error": str(e),
            "tool": tool_name,
            "arguments": arguments
        }


# Synchronous wrappers using asyncio
def list_available_tools():
    """Synchronous wrapper for list_tools_async."""
    try:
        return asyncio.run(list_tools_async())
    except Exception as e:
        return [{"error": str(e)}]


def call_mcp_tool(tool_name: str, arguments: dict):
    """Synchronous wrapper for call_tool_async."""
    try:
        return asyncio.run(call_tool_async(tool_name, arguments))
    except Exception as e:
        return {
            "error": str(e),
            "tool": tool_name,
            "arguments": arguments
        }


# Example usage
if __name__ == "__main__":
    print("Testing MCP Client...")
    
    if not ALPHA_VANTAGE_API_KEY:
        print("\nError: ALPHA_VANTAGE_API_KEY not set")
        print("Please create a .env file with:")
        print("ALPHA_VANTAGE_API_KEY=your-key-here")
        print("\nGet a free key at: https://www.alphavantage.co/support/#api-key")
        sys.exit(1)
    
    # List available tools
    print("\nFetching available tools...")
    tools = list_available_tools()
    
    if tools and "error" not in tools[0]:
        print(f"\n✓ Successfully connected!")
        print(f"Found {len(tools)} tools:\n")
        for i, tool in enumerate(tools[:10], 1):
            print(f"{i}. {tool.get('name')}: {tool.get('description', 'No description')[:80]}")
        if len(tools) > 10:
            print(f"... and {len(tools) - 10} more")
        
        # Test a tool call
        print("\n\nTesting GLOBAL_QUOTE tool with NVDA...")
        result = call_mcp_tool("GLOBAL_QUOTE", {"symbol": "NVDA"})
        print(json.dumps(result, indent=2)[:500] + "...")
        
    else:
        print(f"\n✗ Error: {tools}")
        sys.exit(1)
