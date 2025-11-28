
from servers.mcp_client import call_mcp_tool


def STOCH(params: dict = None) -> dict:
    """
    Returns the stochastic oscillator (STOCH) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            fastkperiod (optional, integer): The time period of the fastk moving average. Positive integers are accepted. By default, fastkperiod=5.
            slowkperiod (optional, integer): The time period of the slowk moving average. Positive integers are accepted. By default, slowkperiod=3.
            slowdperiod (optional, integer): The time period of the slowd moving average. Positive integers are accepted. By default, slowdperiod=3.
            slowkmatype (optional, integer): Moving average type for the slowk moving average. By default, slowkmatype=0.
            slowdmatype (optional, integer): Moving average type for the slowd moving average. By default, slowdmatype=0.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("STOCH", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing STOCH...")
    result = STOCH()
    print(json.dumps(result, indent=2))
