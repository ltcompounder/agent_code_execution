
from servers.mcp_client import call_mcp_tool


def GLOBAL_QUOTE(params: dict = None) -> dict:
    """
    
Returns the latest price and volume information for a ticker.

Args:
    symbol: The symbol of the global ticker. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the latest quote information based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("GLOBAL_QUOTE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing GLOBAL_QUOTE...")
    result = GLOBAL_QUOTE()
    print(json.dumps(result, indent=2))
