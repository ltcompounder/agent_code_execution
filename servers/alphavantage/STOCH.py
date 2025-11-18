
from servers.mcp_client import call_mcp_tool


def STOCH(params: dict = None) -> dict:
    """
    
Returns the stochastic oscillator (STOCH) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastkperiod: The time period of the fastk moving average. Positive integers are accepted. By default, fastkperiod=5.
    slowkperiod: The time period of the slowk moving average. Positive integers are accepted. By default, slowkperiod=3.
    slowdperiod: The time period of the slowd moving average. Positive integers are accepted. By default, slowdperiod=3.
    slowkmatype: Moving average type for the slowk moving average. By default, slowkmatype=0.
                Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
                1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
                3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
                5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
                8 = MESA Adaptive Moving Average (MAMA).
    slowdmatype: Moving average type for the slowd moving average. By default, slowdmatype=0.
                Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
                1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
                3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
                5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
                8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The STOCH values in JSON or CSV format.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("STOCH", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing STOCH...")
    result = STOCH()
    print(json.dumps(result, indent=2))
