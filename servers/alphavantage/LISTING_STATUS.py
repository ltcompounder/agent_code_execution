
from servers.mcp_client import call_mcp_tool


def LISTING_STATUS(params: dict = None) -> dict:
    """
    Returns a list of active or delisted US stocks and ETFs.

Can return data as of the latest trading day or at a specific time in history.
Facilitates equity research on asset lifecycle and survivorship.

Args:
    date: If no date is set, returns symbols as of the latest trading day.
         If set, "travels back" to return symbols on that date in history.
         Any YYYY-MM-DD date later than 2010-01-01 is supported. For example: date=2013-08-03
    state: By default, state=active returns actively traded stocks and ETFs.
          Set state=delisted to query delisted assets.

Returns:
    Listing status data in CSV format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
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
