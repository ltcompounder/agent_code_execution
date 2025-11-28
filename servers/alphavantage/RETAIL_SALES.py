
from servers.mcp_client import call_mcp_tool


def RETAIL_SALES(params: dict = None) -> dict:
    """
    This API returns the monthly Advance Retail Sales: Retail Trade data of the United States.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("RETAIL_SALES", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing RETAIL_SALES...")
    result = RETAIL_SALES()
    print(json.dumps(result, indent=2))
