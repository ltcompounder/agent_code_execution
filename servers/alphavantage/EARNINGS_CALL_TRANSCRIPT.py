
from servers.mcp_client import call_mcp_tool


def EARNINGS_CALL_TRANSCRIPT(params: dict = None) -> dict:
    """
    Returns earnings call transcript for a company in a specific quarter.

Covers 15+ years of history enriched with LLM-based sentiment signals.

Args:
    symbol: Ticker symbol. Example: "IBM".
    quarter: Fiscal quarter in YYYYQM format. Example: "2024Q1". Supports quarters since 2010Q1.
    
Returns:
    Dictionary containing earnings call transcript data or JSON string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("EARNINGS_CALL_TRANSCRIPT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing EARNINGS_CALL_TRANSCRIPT...")
    result = EARNINGS_CALL_TRANSCRIPT()
    print(json.dumps(result, indent=2))
