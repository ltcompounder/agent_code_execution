
from servers.mcp_client import call_mcp_tool


def TIME_SERIES_DAILY_ADJUSTED(params: dict = None) -> dict:
    """
    Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events.

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
    return call_mcp_tool("TIME_SERIES_DAILY_ADJUSTED", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TIME_SERIES_DAILY_ADJUSTED...")
    result = TIME_SERIES_DAILY_ADJUSTED()
    print(json.dumps(result, indent=2))
