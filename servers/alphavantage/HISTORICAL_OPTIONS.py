
from servers.mcp_client import call_mcp_tool


def HISTORICAL_OPTIONS(params: dict = None) -> dict:
    """
    Returns the full historical options chain for a specific symbol on a specific date.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the equity of your choice. For example: symbol=IBM
            date (optional, string): By default, the date parameter is not set and the API will return data for the previous trading session.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
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
