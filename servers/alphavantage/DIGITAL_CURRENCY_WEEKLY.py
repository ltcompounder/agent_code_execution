
from servers.mcp_client import call_mcp_tool


def DIGITAL_CURRENCY_WEEKLY(params: dict = None) -> dict:
    """
    
This API returns the weekly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

Args:
    symbol: The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.
    market: The exchange market of your choice. It can be any of the market in the market list. For example: market=EUR.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the weekly time series in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The weekly time series data in the specified format.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("DIGITAL_CURRENCY_WEEKLY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing DIGITAL_CURRENCY_WEEKLY...")
    result = DIGITAL_CURRENCY_WEEKLY()
    print(json.dumps(result, indent=2))
