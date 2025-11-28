
from servers.mcp_client import call_mcp_tool


def MINUS_DI(params: dict = None) -> dict:
    """
    Returns the minus directional indicator (MINUS_DI) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            time_period (required, integer): Number of data points used to calculate each MINUS_DI value. Positive integers are accepted.
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("MINUS_DI", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing MINUS_DI...")
    result = MINUS_DI()
    print(json.dumps(result, indent=2))
