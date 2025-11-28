
from servers.mcp_client import call_mcp_tool


def MACDEXT(params: dict = None) -> dict:
    """
    Returns the moving average convergence / divergence values with controllable moving average type.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            series_type (required, string): The desired price type in the time series. Four types are supported: close, open, high, low
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            fastperiod (optional, integer): Positive integers are accepted. By default, fastperiod=12.
            slowperiod (optional, integer): Positive integers are accepted. By default, slowperiod=26.
            signalperiod (optional, integer): Positive integers are accepted. By default, signalperiod=9.
            fastmatype (optional, integer): Moving average type for the faster moving average. By default, fastmatype=0.
            slowmatype (optional, integer): Moving average type for the slower moving average. By default, slowmatype=0.
            signalmatype (optional, integer): Moving average type for the signal moving average. By default, signalmatype=0.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("MACDEXT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing MACDEXT...")
    result = MACDEXT()
    print(json.dumps(result, indent=2))
