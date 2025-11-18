
from servers.mcp_client import call_mcp_tool


def TOP_GAINERS_LOSERS(params: dict = None) -> dict:
    """
    Returns top 20 gainers, losers, and most active traded tickers in the US market.

Args:
    None.
    
Returns:
    Dictionary containing top gainers/losers data or JSON string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("TOP_GAINERS_LOSERS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TOP_GAINERS_LOSERS...")
    result = TOP_GAINERS_LOSERS()
    print(json.dumps(result, indent=2))
