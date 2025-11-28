
from servers.mcp_client import call_mcp_tool


def DURABLES(params: dict = None) -> dict:
    """
    This API returns the monthly manufacturers' new orders of durable goods in the United States.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("DURABLES", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing DURABLES...")
    result = DURABLES()
    print(json.dumps(result, indent=2))
