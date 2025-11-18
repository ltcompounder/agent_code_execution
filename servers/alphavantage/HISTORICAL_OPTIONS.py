
from servers.mcp_client import call_mcp_tool


def HISTORICAL_OPTIONS(params: dict = None) -> dict:
    """
    Returns the full historical options chain for a specific symbol on a specific date.

Covers 15+ years of history. Implied volatility (IV) and common Greeks (e.g., delta, gamma, theta, vega, rho) 
are also returned. Option chains are sorted by expiration dates in chronological order. 
Within the same expiration date, contracts are sorted by strike prices from low to high.

Args:
    symbol: The name of the equity of your choice. For example: symbol=IBM
    date: By default, the date parameter is not set and the API will return data for the previous trading session. 
          Any date later than 2008-01-01 is accepted. For example, date=2017-11-15.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the options data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Historical options data in JSON format or CSV string based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("HISTORICAL_OPTIONS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing HISTORICAL_OPTIONS...")
    result = HISTORICAL_OPTIONS()
    print(json.dumps(result, indent=2))
