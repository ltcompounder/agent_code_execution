
from servers.mcp_client import call_mcp_tool


def NEWS_SENTIMENT(params: dict = None) -> dict:
    """
    Returns live and historical market news & sentiment data from premier news outlets worldwide.

Covers stocks, cryptocurrencies, forex, and topics like fiscal policy, mergers & acquisitions, IPOs.

Args:
    tickers: Stock/crypto/forex symbols to filter articles. Example: "IBM" or "COIN,CRYPTO:BTC,FOREX:USD".
    topics: News topics to filter by. Example: "technology" or "technology,ipo".
    time_from: Start time range in YYYYMMDDTHHMM format. Example: "20220410T0130".
    time_to: End time range in YYYYMMDDTHHMM format. Defaults to current time if time_from specified.
    sort: Sort order - "LATEST" (default), "EARLIEST", or "RELEVANCE".
    limit: Number of results to return. Default 50, max 1000.
    
Returns:
    Dictionary containing news sentiment data or JSON string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("NEWS_SENTIMENT", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing NEWS_SENTIMENT...")
    result = NEWS_SENTIMENT()
    print(json.dumps(result, indent=2))
