
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_DAILY_ADJUSTED(params: dict = None) -> dict:
    """
    
Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    outputsize: "compact" (100 data points) or "full" (20+ years of historical data)
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the daily adjusted time series data based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("TIME_SERIES_DAILY_ADJUSTED", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TIME_SERIES_DAILY_ADJUSTED...")
    result = TIME_SERIES_DAILY_ADJUSTED()
    print(json.dumps(result, indent=2))
