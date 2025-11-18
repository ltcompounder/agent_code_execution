
from servers.mcp_client import call_mcp_tool


def UNEMPLOYMENT(params: dict = None) -> dict:
    """
    
This API returns the monthly unemployment data of the United States. The unemployment rate represents the number of 
unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, 
who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions 
(e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Unemployment time series data in JSON format or CSV string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("UNEMPLOYMENT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing UNEMPLOYMENT...")
    result = UNEMPLOYMENT()
    print(json.dumps(result, indent=2))
