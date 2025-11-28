
from servers.mcp_client import call_mcp_tool


def REALTIME_BULK_QUOTES(params: dict = None) -> dict:
    """
    Returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per request.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): Up to 100 symbols separated by comma. Example: MSFT,AAPL,IBM
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("REALTIME_BULK_QUOTES", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing REALTIME_BULK_QUOTES...")
    result = REALTIME_BULK_QUOTES()
    print(json.dumps(result, indent=2))
