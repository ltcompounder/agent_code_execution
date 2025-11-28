
from servers.mcp_client import call_mcp_tool


def PING(params: dict = None) -> dict:
    """
    Check if the service is healthy.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            No parameters required

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("PING", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing PING...")
    result = PING()
    print(json.dumps(result, indent=2))
