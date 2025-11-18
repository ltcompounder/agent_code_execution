
from servers.mcp_client import call_mcp_tool


def PING(params: dict = None) -> dict:
    """
    Check if the service is healthy.
    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("PING", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing PING...")
    result = PING()
    print(json.dumps(result, indent=2))
