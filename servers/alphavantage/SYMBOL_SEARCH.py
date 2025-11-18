
from servers.mcp_client import call_mcp_tool


def SYMBOL_SEARCH(params: dict = None) -> dict:
    """
    
Returns best-matching symbols and market information based on keywords.

Args:
    keywords: A text string of your choice. Example: microsoft
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing symbol search results based on datatype parameter.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("SYMBOL_SEARCH", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing SYMBOL_SEARCH...")
    result = SYMBOL_SEARCH()
    print(json.dumps(result, indent=2))
