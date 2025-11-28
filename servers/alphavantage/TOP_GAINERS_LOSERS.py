
from servers.mcp_client import call_mcp_tool


def TOP_GAINERS_LOSERS(params: dict = None) -> dict:
    """
    Returns top 20 gainers, losers, and most active traded tickers in the US market.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            No parameters required

    Returns:
        dict: API response containing the requested data or error information
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
