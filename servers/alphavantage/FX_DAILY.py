
from servers.mcp_client import call_mcp_tool


def FX_DAILY(params: dict = None) -> dict:
    """
    
This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    outputsize: By default, outputsize=compact. Strings compact and full are accepted with the following specifications: 
               compact returns only the latest 100 data points in the daily time series; 
               full returns the full-length daily time series. The "compact" option is recommended if you would like to reduce the data size of each API call.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Daily FX time series data as a dictionary or string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("FX_DAILY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FX_DAILY...")
    result = FX_DAILY()
    print(json.dumps(result, indent=2))
