
from servers.mcp_client import call_mcp_tool


def HT_TRENDMODE(params: dict = None) -> dict:
    """
    Returns the Hilbert transform, trend vs cycle mode (HT_TRENDMODE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform trend vs cycle mode values in the specified format.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("HT_TRENDMODE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing HT_TRENDMODE...")
    result = HT_TRENDMODE()
    print(json.dumps(result, indent=2))
