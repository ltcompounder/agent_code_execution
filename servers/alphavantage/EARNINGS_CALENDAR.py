
from servers.mcp_client import call_mcp_tool


def EARNINGS_CALENDAR(params: dict = None) -> dict:
    """
    Returns a list of company earnings expected in the next 3, 6, or 12 months.

Args:
    symbol: By default, no symbol is set and returns full list of scheduled earnings.
           If set, returns expected earnings for that specific symbol. For example: symbol=IBM
    horizon: By default, horizon=3month returns earnings in the next 3 months.
            Set horizon=6month or horizon=12month for 6 or 12 months respectively.

Returns:
    Earnings calendar data in CSV format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
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
