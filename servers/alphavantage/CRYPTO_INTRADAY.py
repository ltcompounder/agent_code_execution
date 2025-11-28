
from servers.mcp_client import call_mcp_tool


def CRYPTO_INTRADAY(params: dict = None) -> dict:
    """
    This API returns intraday time series (timestamp, open, high, low, close, volume) of the cryptocurrency specified, updated realtime.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            symbol (required, string): The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=ETH.
            market (required, string): The exchange market of your choice. It can be any of the market in the market list. For example: market=USD.
            interval (required, string): Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
            outputsize (optional, string): By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.
            datatype (optional, string): By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("CRYPTO_INTRADAY", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing CRYPTO_INTRADAY...")
    result = CRYPTO_INTRADAY()
    print(json.dumps(result, indent=2))
