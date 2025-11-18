
from servers.mcp_client import call_mcp_tool


def BALANCE_SHEET(params: dict = None) -> dict:
    """
    Returns annual and quarterly balance sheets with normalized fields.

Fields are mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed 
on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Balance sheet data in JSON format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("BALANCE_SHEET", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing BALANCE_SHEET...")
    result = BALANCE_SHEET()
    print(json.dumps(result, indent=2))
