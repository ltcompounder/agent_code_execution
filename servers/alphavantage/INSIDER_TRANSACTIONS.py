
from servers.mcp_client import call_mcp_tool


def INSIDER_TRANSACTIONS(params: dict = None) -> dict:
    """
    Returns latest and historical insider transactions by key stakeholders.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): Ticker symbol. Example: "IBM".

    Returns:
        dict: API response containing the requested data or error information
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
