
from servers.mcp_client import call_mcp_tool


def AD(params: dict = None) -> dict:
    """
    Returns the Chaikin A/D line (AD) values.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the ticker of your choice. For example: symbol=IBM
            interval (required, string): Time interval between two consecutive data points in the time series.
            month (optional, string): Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("AD", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing AD...")
    result = AD()
    print(json.dumps(result, indent=2))
