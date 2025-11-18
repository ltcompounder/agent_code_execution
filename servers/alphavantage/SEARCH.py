
from servers.mcp_client import call_mcp_tool


def SEARCH(params: dict = None) -> dict:
    """
    
Search for relevant Alpha Vantage data based on natural language query.

Args:
    query: Natural language search query (e.g., "AAPL stock price daily", "Tesla earnings data")

Returns:
    Dictionary with 'results' key containing list of relevant data sources.
    Each result includes id, title, text snippet describing the data, and url.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("SEARCH", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing SEARCH...")
    result = SEARCH()
    print(json.dumps(result, indent=2))
