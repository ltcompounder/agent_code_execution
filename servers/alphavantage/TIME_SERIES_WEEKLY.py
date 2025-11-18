
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_WEEKLY(params: dict = None) -> dict:
    """
    
Returns weekly time series (last trading day of each week, OHLCV) covering 20+ years of historical data.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the weekly time series data based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("TIME_SERIES_WEEKLY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TIME_SERIES_WEEKLY...")
    result = TIME_SERIES_WEEKLY()
    print(json.dumps(result, indent=2))
