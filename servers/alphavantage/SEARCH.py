
from servers.mcp_client import call_mcp_tool


def SEARCH(params: dict = None) -> dict:
    """
    Search for relevant Alpha Vantage data based on natural language query.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            query (required, string): Natural language search query (e.g., "AAPL stock price daily", "Tesla earnings data")

    Returns:
        dict: API response containing the requested data or error information
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
