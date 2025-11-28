
from servers.mcp_client import call_mcp_tool


def CMO(params: dict = None) -> dict:
    """
    Returns the Chande momentum oscillator (CMO) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            time_period (required, integer): Number of data points used to calculate each CMO value. Positive integers are accepted (e.g., time_period=60, time_period=200)
            series_type (required, string): The desired price type in the time series. Four types are supported: close, open, high, low
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("CMO", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CMO...")
    result = CMO()
    print(json.dumps(result, indent=2))
