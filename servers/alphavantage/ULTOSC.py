
from servers.mcp_client import call_mcp_tool


def ULTOSC(params: dict = None) -> dict:
    """
    Returns the ultimate oscillator (ULTOSC) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            timeperiod1 (optional, integer): The first time period for the indicator. Positive integers are accepted. By default, timeperiod1=7.
            timeperiod2 (optional, integer): The second time period for the indicator. Positive integers are accepted. By default, timeperiod2=14.
            timeperiod3 (optional, integer): The third time period for the indicator. Positive integers are accepted. By default, timeperiod3=28.
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("ULTOSC", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing ULTOSC...")
    result = ULTOSC()
    print(json.dumps(result, indent=2))
