
from servers.mcp_client import call_mcp_tool


def FX_MONTHLY(params: dict = None) -> dict:
    """
    
This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Monthly FX time series data as a dictionary or string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("FX_MONTHLY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FX_MONTHLY...")
    result = FX_MONTHLY()
    print(json.dumps(result, indent=2))
