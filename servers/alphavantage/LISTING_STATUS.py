
from servers.mcp_client import call_mcp_tool


def LISTING_STATUS(params: dict = None) -> dict:
    """
    Returns a list of active or delisted US stocks and ETFs.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            date (optional, string): If no date is set, returns symbols as of the latest trading day.
            state (optional, string): By default, state=active returns actively traded stocks and ETFs.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("LISTING_STATUS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing LISTING_STATUS...")
    result = LISTING_STATUS()
    print(json.dumps(result, indent=2))
