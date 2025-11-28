
from servers.mcp_client import call_mcp_tool


def DIGITAL_CURRENCY_MONTHLY(params: dict = None) -> dict:
    """
    This API returns the monthly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.
            market (required, string): The exchange market of your choice. It can be any of the market in the market list. For example: market=EUR.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the data as a CSV (comma separated value) file.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("DIGITAL_CURRENCY_MONTHLY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing DIGITAL_CURRENCY_MONTHLY...")
    result = DIGITAL_CURRENCY_MONTHLY()
    print(json.dumps(result, indent=2))
