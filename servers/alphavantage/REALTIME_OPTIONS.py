
from servers.mcp_client import call_mcp_tool


def REALTIME_OPTIONS(params: dict = None) -> dict:
    """
    Returns realtime US options data with full market coverage.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The name of the equity of your choice. For example: symbol=IBM
            require_greeks (optional, boolean): Enable greeks & implied volatility (IV) fields. By default, require_greeks=false.
            contract (optional, string): The US options contract ID you would like to specify. By default, the contract parameter
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:
            entitlement (optional, string): "delayed" for 15-minute delayed data, "realtime" for realtime data

    Returns:
        dict: API response containing the requested data or error information
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
