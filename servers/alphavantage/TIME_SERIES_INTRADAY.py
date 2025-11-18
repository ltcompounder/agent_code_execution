
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_INTRADAY(params: dict = None) -> dict:
    """
    
Returns current and 20+ years of historical intraday OHLCV time series of the equity specified.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    interval: Time interval between consecutive data points. Supported: 1min, 5min, 15min, 30min, 60min
    adjusted: By default True. Set False to query raw (as-traded) intraday values
    extended_hours: By default True. Set False for regular trading hours only
    month: Query specific month in YYYY-MM format. Example: 2009-01
    outputsize: "compact" (100 data points) or "full" (30 days or full month)
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the time series data based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("TIME_SERIES_INTRADAY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TIME_SERIES_INTRADAY...")
    result = TIME_SERIES_INTRADAY()
    print(json.dumps(result, indent=2))
