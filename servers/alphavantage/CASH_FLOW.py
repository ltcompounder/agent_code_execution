
from servers.mcp_client import call_mcp_tool


def CASH_FLOW(params: dict = None) -> dict:
    """
    Returns annual and quarterly cash flow with normalized fields.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=IBM.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("CASH_FLOW", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CASH_FLOW...")
    result = CASH_FLOW()
    print(json.dumps(result, indent=2))
