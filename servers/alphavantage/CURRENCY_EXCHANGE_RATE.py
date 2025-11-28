
from servers.mcp_client import call_mcp_tool


def CURRENCY_EXCHANGE_RATE(params: dict = None) -> dict:
    """
    This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            from_currency (required, string): The currency you would like to get the exchange rate for. It can either be a physical currency
            to_currency (required, string): The destination currency for the exchange rate. It can either be a physical currency

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("CURRENCY_EXCHANGE_RATE", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CURRENCY_EXCHANGE_RATE...")
    result = CURRENCY_EXCHANGE_RATE()
    print(json.dumps(result, indent=2))
