
from servers.mcp_client import call_mcp_tool


def ADD_TWO_NUMBERS(params: dict = None) -> dict:
    """
    Add two numbers together.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            a (required, integer): Parameter a
            b (required, integer): Parameter b

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("ADD_TWO_NUMBERS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing ADD_TWO_NUMBERS...")
    result = ADD_TWO_NUMBERS()
    print(json.dumps(result, indent=2))
