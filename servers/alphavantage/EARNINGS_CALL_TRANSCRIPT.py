
from servers.mcp_client import call_mcp_tool


def EARNINGS_CALL_TRANSCRIPT(params: dict = None) -> dict:
    """
    Returns earnings call transcript for a company in a specific quarter.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): Ticker symbol. Example: "IBM".
            quarter (required, string): Fiscal quarter in YYYYQM format. Example: "2024Q1". Supports quarters since 2010Q1.

    Returns:
        dict: API response containing the requested data or error information
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
