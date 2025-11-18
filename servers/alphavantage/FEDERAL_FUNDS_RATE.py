
from servers.mcp_client import call_mcp_tool


def FEDERAL_FUNDS_RATE(params: dict = None) -> dict:
    """
    
This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.

Args:
    interval: By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Federal funds rate time series data in JSON format or CSV string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("FEDERAL_FUNDS_RATE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FEDERAL_FUNDS_RATE...")
    result = FEDERAL_FUNDS_RATE()
    print(json.dumps(result, indent=2))
