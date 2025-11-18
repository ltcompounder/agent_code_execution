
from servers.mcp_client import call_mcp_tool


def BRENT(params: dict = None) -> dict:
    """
    
This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.

Args:
    interval: By default, monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Brent crude oil price data in the specified format.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("BRENT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing BRENT...")
    result = BRENT()
    print(json.dumps(result, indent=2))
