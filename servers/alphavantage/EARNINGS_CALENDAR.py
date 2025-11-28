
from servers.mcp_client import call_mcp_tool


def EARNINGS_CALENDAR(params: dict = None) -> dict:
    """
    Returns a list of company earnings expected in the next 3, 6, or 12 months.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (optional, string): By default, no symbol is set and returns full list of scheduled earnings.
            horizon (optional, string): By default, horizon=3month returns earnings in the next 3 months.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("EARNINGS_CALENDAR", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing EARNINGS_CALENDAR...")
    result = EARNINGS_CALENDAR()
    print(json.dumps(result, indent=2))
