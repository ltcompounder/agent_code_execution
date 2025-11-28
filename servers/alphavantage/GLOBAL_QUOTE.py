
from servers.mcp_client import call_mcp_tool


def GLOBAL_QUOTE(params: dict = None) -> dict:
    """
    Returns the latest price and volume information for a ticker.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the global ticker. For example: symbol=IBM
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
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
