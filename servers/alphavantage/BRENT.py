
from servers.mcp_client import call_mcp_tool


def BRENT(params: dict = None) -> dict:
    """
    This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            interval (optional, string): By default, monthly. Strings daily, weekly, and monthly are accepted.
            datatype (optional, string): By default, csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("BRENT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing BRENT...")
    result = BRENT()
    print(json.dumps(result, indent=2))
