
from servers.mcp_client import call_mcp_tool


def MARKET_STATUS(params: dict = None) -> dict:
    """
    
Returns the current market status (open vs. closed) of major trading venues worldwide.

Returns:
    Dict containing current market status information.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("MARKET_STATUS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing MARKET_STATUS...")
    result = MARKET_STATUS()
    print(json.dumps(result, indent=2))
