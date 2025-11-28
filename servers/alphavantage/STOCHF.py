
from servers.mcp_client import call_mcp_tool


def STOCHF(params: dict = None) -> dict:
    """
    Returns the stochastic fast (STOCHF) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            fastkperiod (optional, integer): The time period of the fastk moving average. Positive integers are accepted. By default, fastkperiod=5.
            fastdperiod (optional, integer): The time period of the fastd moving average. Positive integers are accepted. By default, fastdperiod=3.
            fastdmatype (optional, integer): Moving average type for the fastd moving average. By default, fastdmatype=0.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("STOCHF", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing STOCHF...")
    result = STOCHF()
    print(json.dumps(result, indent=2))
