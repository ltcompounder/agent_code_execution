
from servers.mcp_client import call_mcp_tool


def COMPANY_OVERVIEW(params: dict = None) -> dict:
    """
    Returns company information, financial ratios, and key metrics for the specified equity.

Data is generally refreshed on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Company overview data in JSON format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("COMPANY_OVERVIEW", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing COMPANY_OVERVIEW...")
    result = COMPANY_OVERVIEW()
    print(json.dumps(result, indent=2))
