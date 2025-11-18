
from servers.mcp_client import call_mcp_tool


def CURRENCY_EXCHANGE_RATE(params: dict = None) -> dict:
    """
    
This API returns the realtime exchange rate for any pair of digital currency (e.g., Bitcoin) or physical currency (e.g., USD).

Args:
    from_currency: The currency you would like to get the exchange rate for. It can either be a physical currency or digital/crypto currency. For example: from_currency=USD or from_currency=BTC.
    to_currency: The destination currency for the exchange rate. It can either be a physical currency or digital/crypto currency. For example: to_currency=USD or to_currency=BTC.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the exchange rate in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The exchange rate data in the specified format.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
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
