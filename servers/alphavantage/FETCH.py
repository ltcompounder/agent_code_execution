
from servers.mcp_client import call_mcp_tool


def FETCH(params: dict = None) -> dict:
    """
    
Fetch complete financial data by calling the specified Alpha Vantage API function.

Args:
    id: Alpha Vantage API function name (from search results)

Returns:
    Complete data response with id, title, full data content, URL, and metadata

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("FETCH", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FETCH...")
    result = FETCH()
    print(json.dumps(result, indent=2))
