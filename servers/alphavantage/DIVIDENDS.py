
from servers.mcp_client import call_mcp_tool


def DIVIDENDS(params: dict = None) -> dict:
    """
    Returns historical and future (declared) dividend distributions.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.
    datatype: By default, datatype=csv. Strings json and csv are accepted.
             json returns the data in JSON format; csv returns as CSV file.

Returns:
    Dividend data in specified format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("DIVIDENDS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing DIVIDENDS...")
    result = DIVIDENDS()
    print(json.dumps(result, indent=2))
