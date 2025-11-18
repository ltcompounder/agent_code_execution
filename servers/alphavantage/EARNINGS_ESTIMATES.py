
from servers.mcp_client import call_mcp_tool


def EARNINGS_ESTIMATES(params: dict = None) -> dict:
    """
    Returns annual and quarterly EPS and revenue estimates with analyst data.

Includes analyst count and revision history.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Earnings estimates data in JSON format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("EARNINGS_ESTIMATES", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing EARNINGS_ESTIMATES...")
    result = EARNINGS_ESTIMATES()
    print(json.dumps(result, indent=2))
