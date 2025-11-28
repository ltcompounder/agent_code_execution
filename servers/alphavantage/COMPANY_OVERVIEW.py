
from servers.mcp_client import call_mcp_tool


def COMPANY_OVERVIEW(params: dict = None) -> dict:
    """
    Returns company information, financial ratios, and key metrics for the specified equity.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=IBM.

    Returns:
        dict: API response containing the requested data or error information
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
