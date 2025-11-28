
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_DAILY(params: dict = None) -> dict:
    """
    Returns raw daily time series (OHLCV) of the global equity specified, covering 20+ years of historical data.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the equity. For example: symbol=IBM
            outputsize (optional, string): "compact" (100 data points) or "full" (20+ years of historical data)
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("TIME_SERIES_DAILY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TIME_SERIES_DAILY...")
    result = TIME_SERIES_DAILY()
    print(json.dumps(result, indent=2))
