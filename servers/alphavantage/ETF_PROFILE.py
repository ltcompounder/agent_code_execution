
from servers.mcp_client import call_mcp_tool


def ETF_PROFILE(params: dict = None) -> dict:
    """
    Returns key ETF metrics and holdings with allocation by asset types and sectors.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=QQQ.

    Returns:
        dict: API response containing the requested data or error information
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
