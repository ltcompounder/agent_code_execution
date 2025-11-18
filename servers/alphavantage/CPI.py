
from servers.mcp_client import call_mcp_tool


def CPI(params: dict = None) -> dict:
    """
    
This API returns the monthly and semiannual consumer price index (CPI) of the United States. 
CPI is widely regarded as the barometer of inflation levels in the broader economy.

Args:
    interval: By default, interval=monthly. Strings monthly and semiannual are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    CPI time series data in JSON format or CSV string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("CPI", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CPI...")
    result = CPI()
    print(json.dumps(result, indent=2))
