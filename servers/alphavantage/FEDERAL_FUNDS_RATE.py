
from servers.mcp_client import call_mcp_tool


def FEDERAL_FUNDS_RATE(params: dict = None) -> dict:
    """
    This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            interval (optional, string): By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications:

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("FEDERAL_FUNDS_RATE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing FEDERAL_FUNDS_RATE...")
    result = FEDERAL_FUNDS_RATE()
    print(json.dumps(result, indent=2))
