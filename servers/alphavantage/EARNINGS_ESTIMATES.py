
from servers.mcp_client import call_mcp_tool


def EARNINGS_ESTIMATES(params: dict = None) -> dict:
    """
    Returns annual and quarterly EPS and revenue estimates with analyst data.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=IBM.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("EARNINGS_ESTIMATES", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing EARNINGS_ESTIMATES...")
    result = EARNINGS_ESTIMATES()
    print(json.dumps(result, indent=2))
