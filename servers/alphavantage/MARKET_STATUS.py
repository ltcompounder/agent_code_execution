
from servers.mcp_client import call_mcp_tool


def MARKET_STATUS(params: dict = None) -> dict:
    """
    Returns the current market status (open vs. closed) of major trading venues worldwide.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("MARKET_STATUS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing MARKET_STATUS...")
    result = MARKET_STATUS()
    print(json.dumps(result, indent=2))
