
from servers.mcp_client import call_mcp_tool


def ADD_TWO_NUMBERS(params: dict = None) -> dict:
    """
    Add two numbers together.
    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("ADD_TWO_NUMBERS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing ADD_TWO_NUMBERS...")
    result = ADD_TWO_NUMBERS()
    print(json.dumps(result, indent=2))
