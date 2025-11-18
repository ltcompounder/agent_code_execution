
from servers.mcp_client import call_mcp_tool


def REALTIME_OPTIONS(params: dict = None) -> dict:
    """
    Returns realtime US options data with full market coverage.

Option chains are sorted by expiration dates in chronological order. 
Within the same expiration date, contracts are sorted by strike prices from low to high.

Args:
    symbol: The name of the equity of your choice. For example: symbol=IBM
    require_greeks: Enable greeks & implied volatility (IV) fields. By default, require_greeks=false. 
                   Set require_greeks=true to enable greeks & IVs in the API response.
    contract: The US options contract ID you would like to specify. By default, the contract parameter 
             is not set and the entire option chain for a given symbol will be returned.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the options data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Realtime options data in JSON format or CSV string based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("REALTIME_OPTIONS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing REALTIME_OPTIONS...")
    result = REALTIME_OPTIONS()
    print(json.dumps(result, indent=2))
