
from servers.mcp_client import call_mcp_tool


def TREASURY_YIELD(params: dict = None) -> dict:
    """
    This API returns the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            interval (optional, string): By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
            maturity (optional, string): By default, maturity=10year. Strings 3month, 2year, 5year, 7year, 10year, and 30year are accepted.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("TREASURY_YIELD", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing TREASURY_YIELD...")
    result = TREASURY_YIELD()
    print(json.dumps(result, indent=2))
