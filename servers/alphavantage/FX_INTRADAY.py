
from servers.mcp_client import call_mcp_tool


def FX_INTRADAY(params: dict = None) -> dict:
    """
    This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            from_symbol (required, string): A three-letter symbol from the forex currency list. For example: from_symbol=EUR
            to_symbol (required, string): A three-letter symbol from the forex currency list. For example: to_symbol=USD
            interval (required, string): Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
            outputsize (optional, string): By default, outputsize=compact. Strings compact and full are accepted with the following specifications:
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("FX_INTRADAY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FX_INTRADAY...")
    result = FX_INTRADAY()
    print(json.dumps(result, indent=2))
