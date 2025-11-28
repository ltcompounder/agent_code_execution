
from servers.mcp_client import call_mcp_tool


def REAL_GDP(params: dict = None) -> dict:
    """
    This API returns the annual and quarterly Real GDP of the United States.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            interval (optional, string): By default, interval=annual. Strings quarterly and annual are accepted.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("REAL_GDP", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing REAL_GDP...")
    result = REAL_GDP()
    print(json.dumps(result, indent=2))
