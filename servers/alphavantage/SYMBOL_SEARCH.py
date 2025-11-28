
from servers.mcp_client import call_mcp_tool


def SYMBOL_SEARCH(params: dict = None) -> dict:
    """
    Returns best-matching symbols and market information based on keywords.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            keywords (required, string): A text string of your choice. Example: microsoft
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
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
