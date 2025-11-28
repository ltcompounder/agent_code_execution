
from servers.mcp_client import call_mcp_tool


def NEWS_SENTIMENT(params: dict = None) -> dict:
    """
    Returns live and historical market news & sentiment data from premier news outlets worldwide.

    Args:
        params (dict, optional): Dictionary containing the following parameters:
            tickers (optional, string): Stock/crypto/forex symbols to filter articles. Example: "IBM" or "COIN,CRYPTO:BTC,FOREX:USD".
            topics (optional, string): News topics to filter by. Example: "technology" or "technology,ipo".
            time_from (optional, string): Start time range in YYYYMMDDTHHMM format. Example: "20220410T0130".
            time_to (optional, string): End time range in YYYYMMDDTHHMM format. Defaults to current time if time_from specified.
            sort (optional, string): Sort order - "LATEST" (default), "EARLIEST", or "RELEVANCE".
            limit (optional, integer): Number of results to return. Default 50, max 1000.

    Returns:
        dict: API response containing the requested data or error information
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
