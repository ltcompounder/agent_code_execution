
from servers.mcp_client import call_mcp_tool


def ETF_PROFILE(params: dict = None) -> dict:
    """
    Returns key ETF metrics and holdings with allocation by asset types and sectors.

Includes net assets, expense ratio, turnover, and corresponding ETF holdings/constituents.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=QQQ.

Returns:
    ETF profile data in JSON format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("ETF_PROFILE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing ETF_PROFILE...")
    result = ETF_PROFILE()
    print(json.dumps(result, indent=2))
