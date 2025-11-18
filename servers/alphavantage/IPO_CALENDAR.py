
from servers.mcp_client import call_mcp_tool


def IPO_CALENDAR(params: dict = None) -> dict:
    """
    Returns a list of IPOs expected in the next 3 months.

Returns:
    IPO calendar data in CSV format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
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
