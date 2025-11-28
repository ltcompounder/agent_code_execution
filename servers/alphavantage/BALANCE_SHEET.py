
from servers.mcp_client import call_mcp_tool


def BALANCE_SHEET(params: dict = None) -> dict:
    """
    Returns annual and quarterly balance sheets with normalized fields.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=IBM.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("BALANCE_SHEET", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing BALANCE_SHEET...")
    result = BALANCE_SHEET()
    print(json.dumps(result, indent=2))
