
from servers.mcp_client import call_mcp_tool


def INSIDER_TRANSACTIONS(params: dict = None) -> dict:
    """
    Returns latest and historical insider transactions by key stakeholders.

Covers transactions by founders, executives, board members, etc.

Args:
    symbol: Ticker symbol. Example: "IBM".
    
Returns:
    Dictionary containing insider transaction data or JSON string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("INSIDER_TRANSACTIONS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing INSIDER_TRANSACTIONS...")
    result = INSIDER_TRANSACTIONS()
    print(json.dumps(result, indent=2))
