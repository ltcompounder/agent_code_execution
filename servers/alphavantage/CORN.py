
from servers.mcp_client import call_mcp_tool


def CORN(params: dict = None) -> dict:
    """
    This API returns the global price of corn in monthly, quarterly, and annual horizons.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            interval (optional, string): By default, monthly. Strings monthly, quarterly, and annual are accepted.
            datatype (optional, string): By default, csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("CORN", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CORN...")
    result = CORN()
    print(json.dumps(result, indent=2))
