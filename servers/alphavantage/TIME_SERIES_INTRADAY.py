
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_INTRADAY(params: dict = None) -> dict:
    """
    Returns current and 20+ years of historical intraday OHLCV time series of the equity specified.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the equity. For example: symbol=IBM
            interval (required, string): Time interval between consecutive data points. Supported: 1min, 5min, 15min, 30min, 60min
            adjusted (optional, boolean): By default True. Set False to query raw (as-traded) intraday values
            extended_hours (optional, boolean): By default True. Set False for regular trading hours only
            month (optional, string): Query specific month in YYYY-MM format. Example: 2009-01
            outputsize (optional, string): "compact" (100 data points) or "full" (30 days or full month)
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
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
