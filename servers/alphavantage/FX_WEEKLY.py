
from servers.mcp_client import call_mcp_tool


def FX_WEEKLY(params: dict = None) -> dict:
    """
    This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            from_symbol (required, string): A three-letter symbol from the forex currency list. For example: from_symbol=EUR
            to_symbol (required, string): A three-letter symbol from the forex currency list. For example: to_symbol=USD
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("FX_WEEKLY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FX_WEEKLY...")
    result = FX_WEEKLY()
    print(json.dumps(result, indent=2))
