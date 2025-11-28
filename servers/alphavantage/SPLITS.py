
from servers.mcp_client import call_mcp_tool


def SPLITS(params: dict = None) -> dict:
    """
    Returns historical split events.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The symbol of the ticker of your choice. For example: symbol=IBM.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("SPLITS", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing SPLITS...")
    result = SPLITS()
    print(json.dumps(result, indent=2))
