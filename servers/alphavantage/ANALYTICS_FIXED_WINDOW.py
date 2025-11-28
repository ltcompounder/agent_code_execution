
from servers.mcp_client import call_mcp_tool


def ANALYTICS_FIXED_WINDOW(params: dict = None) -> dict:
    """
    Returns advanced analytics metrics for time series over a fixed temporal window.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbols (required, string): Comma-separated list of symbols. Free keys: up to 5, Premium keys: up to 50.
            range_param (required, string): Date range for the series. Defaults to full equity history.
            interval (required, string): Time interval - 1min, 5min, 15min, 30min, 60min, DAILY, WEEKLY, MONTHLY.
            calculations (required, string): Comma-separated list of analytics metrics to calculate.
            ohlc (optional, string): OHLC field for calculation - open, high, low, close. Default "close".

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("ANALYTICS_FIXED_WINDOW", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing ANALYTICS_FIXED_WINDOW...")
    result = ANALYTICS_FIXED_WINDOW()
    print(json.dumps(result, indent=2))
