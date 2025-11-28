
from servers.mcp_client import call_mcp_tool


def IPO_CALENDAR(params: dict = None) -> dict:
    """
    Returns a list of IPOs expected in the next 3 months.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            No parameters required

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("IPO_CALENDAR", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing IPO_CALENDAR...")
    result = IPO_CALENDAR()
    print(json.dumps(result, indent=2))
