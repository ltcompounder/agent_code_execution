
from servers.mcp_client import call_mcp_tool


def EARNINGS(params: dict = None) -> dict:
    """
    Returns annual and quarterly earnings (EPS) for the company.

Quarterly data also includes analyst estimates and surprise metrics.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Earnings data in JSON format or error message.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("EARNINGS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing EARNINGS...")
    result = EARNINGS()
    print(json.dumps(result, indent=2))
