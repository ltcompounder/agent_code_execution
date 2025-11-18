
from servers.mcp_client import call_mcp_tool


def INFLATION(params: dict = None) -> dict:
    """
    
This API returns the annual inflation rates (consumer prices) of the United States.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Inflation rate time series data in JSON format or CSV string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("INFLATION", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing INFLATION...")
    result = INFLATION()
    print(json.dumps(result, indent=2))
