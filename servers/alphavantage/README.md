# Alpha Vantage MCP Tools

This directory contains Python wrappers for all Alpha Vantage MCP tools.

## Available Tools (118 total)


### Alpha Intelligence

- **ANALYTICS_FIXED_WINDOW**: Returns advanced analytics metrics for time series over a fixed temporal window.

Calculates metrics like total return, variance, auto-correlation, etc.

Args:
    symbols: Comma-separated list of symbols. Free keys: up to 5, Premium keys: up to 50.
    range_param: Date range for the series. Defaults to full equity history.
    interval: Time interval - 1min, 5min, 15min, 30min, 60min, DAILY, WEEKLY, MONTHLY.
    calculations: Comma-separated list of analytics metrics to calculate.
    ohlc: OHLC field for calculation - open, high, low, close. Default "close".
    
Returns:
    Dictionary containing analytics data or JSON string.

- **ANALYTICS_SLIDING_WINDOW**: Returns advanced analytics metrics for time series over sliding time windows.

Calculates moving metrics like variance over time periods. Example: moving variance over 5 years with 100-point window.

Args:
    symbols: Comma-separated list of symbols. Free keys: up to 5, Premium keys: up to 50.
    range_param: Date range for the series. Defaults to full equity history.
    interval: Time interval - 1min, 5min, 15min, 30min, 60min, DAILY, WEEKLY, MONTHLY.
    window_size: Size of moving window. Minimum 10, larger recommended for statistical significance.
    calculations: Comma-separated analytics metrics. Free keys: 1 metric, Premium keys: multiple.
    ohlc: OHLC field for calculation - open, high, low, close. Default "close".
    
Returns:
    Dictionary containing sliding window analytics data or JSON string.

- **EARNINGS**: Returns annual and quarterly earnings (EPS) for the company.

Quarterly data also includes analyst estimates and surprise metrics.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Earnings data in JSON format or error message.

- **EARNINGS_CALENDAR**: Returns a list of company earnings expected in the next 3, 6, or 12 months.

Args:
    symbol: By default, no symbol is set and returns full list of scheduled earnings.
           If set, returns expected earnings for that specific symbol. For example: symbol=IBM
    horizon: By default, horizon=3month returns earnings in the next 3 months.
            Set horizon=6month or horizon=12month for 6 or 12 months respectively.

Returns:
    Earnings calendar data in CSV format or error message.

- **EARNINGS_CALL_TRANSCRIPT**: Returns earnings call transcript for a company in a specific quarter.

Covers 15+ years of history enriched with LLM-based sentiment signals.

Args:
    symbol: Ticker symbol. Example: "IBM".
    quarter: Fiscal quarter in YYYYQM format. Example: "2024Q1". Supports quarters since 2010Q1.
    
Returns:
    Dictionary containing earnings call transcript data or JSON string.

- **EARNINGS_ESTIMATES**: Returns annual and quarterly EPS and revenue estimates with analyst data.

Includes analyst count and revision history.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Earnings estimates data in JSON format or error message.

- **INSIDER_TRANSACTIONS**: Returns latest and historical insider transactions by key stakeholders.

Covers transactions by founders, executives, board members, etc.

Args:
    symbol: Ticker symbol. Example: "IBM".
    
Returns:
    Dictionary containing insider transaction data or JSON string.

- **NEWS_SENTIMENT**: Returns live and historical market news & sentiment data from premier news outlets worldwide.

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

- **TOP_GAINERS_LOSERS**: Returns top 20 gainers, losers, and most active traded tickers in the US market.

Args:
    None.
    
Returns:
    Dictionary containing top gainers/losers data or JSON string.


### Commodities

- **ALL_COMMODITIES**: 
This API returns the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    All commodities price index data in the specified format.

- **BRENT**: 
This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.

Args:
    interval: By default, monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Brent crude oil price data in the specified format.

- **COPPER**: 
This API returns the global price of copper in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Copper price data in the specified format.

- **NATURAL_GAS**: 
This API returns the Henry Hub natural gas spot prices in daily, weekly, and monthly horizons.

Args:
    interval: By default, monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Natural gas price data in the specified format.

- **WHEAT**: 
This API returns the global price of wheat in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Wheat price data in the specified format.

- **WTI**: 
This API returns the West Texas Intermediate (WTI) crude oil prices in daily, weekly, and monthly horizons.

Args:
    interval: By default, monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    WTI crude oil price data in the specified format.


### Core Stock APIs

- **GLOBAL_QUOTE**: 
Returns the latest price and volume information for a ticker.

Args:
    symbol: The symbol of the global ticker. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the latest quote information based on datatype parameter.

- **MARKET_STATUS**: 
Returns the current market status (open vs. closed) of major trading venues worldwide.

Returns:
    Dict containing current market status information.

- **REALTIME_BULK_QUOTES**: 
Returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per request.

Args:
    symbol: Up to 100 symbols separated by comma. Example: MSFT,AAPL,IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing realtime bulk quotes based on datatype parameter.

- **SEARCH**: 
Search for relevant Alpha Vantage data based on natural language query.

Args:
    query: Natural language search query (e.g., "AAPL stock price daily", "Tesla earnings data")

Returns:
    Dictionary with 'results' key containing list of relevant data sources.
    Each result includes id, title, text snippet describing the data, and url.

- **SYMBOL_SEARCH**: 
Returns best-matching symbols and market information based on keywords.

Args:
    keywords: A text string of your choice. Example: microsoft
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing symbol search results based on datatype parameter.

- **TIME_SERIES_DAILY**: 
Returns raw daily time series (OHLCV) of the global equity specified, covering 20+ years of historical data.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    outputsize: "compact" (100 data points) or "full" (20+ years of historical data)
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the daily time series data based on datatype parameter.

- **TIME_SERIES_DAILY_ADJUSTED**: 
Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    outputsize: "compact" (100 data points) or "full" (20+ years of historical data)
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the daily adjusted time series data based on datatype parameter.

- **TIME_SERIES_INTRADAY**: 
Returns current and 20+ years of historical intraday OHLCV time series of the equity specified.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    interval: Time interval between consecutive data points. Supported: 1min, 5min, 15min, 30min, 60min
    adjusted: By default True. Set False to query raw (as-traded) intraday values
    extended_hours: By default True. Set False for regular trading hours only
    month: Query specific month in YYYY-MM format. Example: 2009-01
    outputsize: "compact" (100 data points) or "full" (30 days or full month)
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the time series data based on datatype parameter.

- **TIME_SERIES_MONTHLY**: 
Returns monthly time series (last trading day of each month, OHLCV) covering 20+ years.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the monthly time series data based on datatype parameter.

- **TIME_SERIES_MONTHLY_ADJUSTED**: 
Returns monthly adjusted time series (OHLCV, adjusted close, volume, dividend) covering 20+ years.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the monthly adjusted time series data based on datatype parameter.

- **TIME_SERIES_WEEKLY**: 
Returns weekly time series (last trading day of each week, OHLCV) covering 20+ years of historical data.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the weekly time series data based on datatype parameter.

- **TIME_SERIES_WEEKLY_ADJUSTED**: 
Returns weekly adjusted time series (OHLCV, adjusted close, volume, dividend) covering 20+ years.

Args:
    symbol: The name of the equity. For example: symbol=IBM
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Dict or string containing the weekly adjusted time series data based on datatype parameter.


### Cryptocurrencies

- **CURRENCY_EXCHANGE_RATE**: 
This API returns the realtime exchange rate for any pair of digital currency (e.g., Bitcoin) or physical currency (e.g., USD).

Args:
    from_currency: The currency you would like to get the exchange rate for. It can either be a physical currency or digital/crypto currency. For example: from_currency=USD or from_currency=BTC.
    to_currency: The destination currency for the exchange rate. It can either be a physical currency or digital/crypto currency. For example: to_currency=USD or to_currency=BTC.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the exchange rate in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The exchange rate data in the specified format.

- **DIGITAL_CURRENCY_DAILY**: 
This API returns the daily historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

Args:
    symbol: The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.
    market: The exchange market of your choice. It can be any of the market in the market list. For example: market=EUR.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the daily time series in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The daily time series data in the specified format.

- **DIGITAL_CURRENCY_MONTHLY**: 
This API returns the monthly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

Args:
    symbol: The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.
    market: The exchange market of your choice. It can be any of the market in the market list. For example: market=EUR.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the monthly time series in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The monthly time series data in the specified format.

- **DIGITAL_CURRENCY_WEEKLY**: 
This API returns the weekly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

Args:
    symbol: The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=BTC.
    market: The exchange market of your choice. It can be any of the market in the market list. For example: market=EUR.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the weekly time series in JSON format; csv returns the data as a CSV (comma separated value) file.

Returns:
    The weekly time series data in the specified format.


### Economic Indicators

- **CPI**: 
This API returns the monthly and semiannual consumer price index (CPI) of the United States. 
CPI is widely regarded as the barometer of inflation levels in the broader economy.

Args:
    interval: By default, interval=monthly. Strings monthly and semiannual are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    CPI time series data in JSON format or CSV string.

- **FEDERAL_FUNDS_RATE**: 
This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.

Args:
    interval: By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Federal funds rate time series data in JSON format or CSV string.

- **INFLATION**: 
This API returns the annual inflation rates (consumer prices) of the United States.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Inflation rate time series data in JSON format or CSV string.

- **REAL_GDP**: 
This API returns the annual and quarterly Real GDP of the United States.

Args:
    interval: By default, interval=annual. Strings quarterly and annual are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Real GDP time series data in JSON format or CSV string.

- **REAL_GDP_PER_CAPITA**: 
This API returns the quarterly Real GDP per Capita data of the United States.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Real GDP per capita time series data in JSON format or CSV string.

- **TREASURY_YIELD**: 
This API returns the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).

Args:
    interval: By default, interval=monthly. Strings daily, weekly, and monthly are accepted.
    maturity: By default, maturity=10year. Strings 3month, 2year, 5year, 7year, 10year, and 30year are accepted.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Treasury yield time series data in JSON format or CSV string.

- **UNEMPLOYMENT**: 
This API returns the monthly unemployment data of the United States. The unemployment rate represents the number of 
unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, 
who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions 
(e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Unemployment time series data in JSON format or CSV string.


### Forex

- **FX_DAILY**: 
This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    outputsize: By default, outputsize=compact. Strings compact and full are accepted with the following specifications: 
               compact returns only the latest 100 data points in the daily time series; 
               full returns the full-length daily time series. The "compact" option is recommended if you would like to reduce the data size of each API call.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Daily FX time series data as a dictionary or string.

- **FX_INTRADAY**: 
This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
    outputsize: By default, outputsize=compact. Strings compact and full are accepted with the following specifications: 
               compact returns only the latest 100 data points in the intraday time series; 
               full returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Intraday FX time series data as a dictionary or string.

- **FX_MONTHLY**: 
This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the monthly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Monthly FX time series data as a dictionary or string.

- **FX_WEEKLY**: 
This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.

Args:
    from_symbol: A three-letter symbol from the forex currency list. For example: from_symbol=EUR
    to_symbol: A three-letter symbol from the forex currency list. For example: to_symbol=USD
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the weekly time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Weekly FX time series data as a dictionary or string.


### Fundamental Data

- **BALANCE_SHEET**: Returns annual and quarterly balance sheets with normalized fields.

Fields are mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed 
on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Balance sheet data in JSON format or error message.

- **CASH_FLOW**: Returns annual and quarterly cash flow with normalized fields.

Fields are mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed 
on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Cash flow data in JSON format or error message.

- **COMPANY_OVERVIEW**: Returns company information, financial ratios, and key metrics for the specified equity.

Data is generally refreshed on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Company overview data in JSON format or error message.

- **INCOME_STATEMENT**: Returns annual and quarterly income statements with normalized fields.

Fields are mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed 
on the same day a company reports its latest earnings and financials.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.

Returns:
    Income statement data in JSON format or error message.

- **IPO_CALENDAR**: Returns a list of IPOs expected in the next 3 months.

Returns:
    IPO calendar data in CSV format or error message.

- **LISTING_STATUS**: Returns a list of active or delisted US stocks and ETFs.

Can return data as of the latest trading day or at a specific time in history.
Facilitates equity research on asset lifecycle and survivorship.

Args:
    date: If no date is set, returns symbols as of the latest trading day.
         If set, "travels back" to return symbols on that date in history.
         Any YYYY-MM-DD date later than 2010-01-01 is supported. For example: date=2013-08-03
    state: By default, state=active returns actively traded stocks and ETFs.
          Set state=delisted to query delisted assets.

Returns:
    Listing status data in CSV format or error message.


### Options Data

- **HISTORICAL_OPTIONS**: Returns the full historical options chain for a specific symbol on a specific date.

Covers 15+ years of history. Implied volatility (IV) and common Greeks (e.g., delta, gamma, theta, vega, rho) 
are also returned. Option chains are sorted by expiration dates in chronological order. 
Within the same expiration date, contracts are sorted by strike prices from low to high.

Args:
    symbol: The name of the equity of your choice. For example: symbol=IBM
    date: By default, the date parameter is not set and the API will return data for the previous trading session. 
          Any date later than 2008-01-01 is accepted. For example, date=2017-11-15.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the options data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Historical options data in JSON format or CSV string based on datatype parameter.

- **REALTIME_OPTIONS**: Returns realtime US options data with full market coverage.

Option chains are sorted by expiration dates in chronological order. 
Within the same expiration date, contracts are sorted by strike prices from low to high.

Args:
    symbol: The name of the equity of your choice. For example: symbol=IBM
    require_greeks: Enable greeks & implied volatility (IV) fields. By default, require_greeks=false. 
                   Set require_greeks=true to enable greeks & IVs in the API response.
    contract: The US options contract ID you would like to specify. By default, the contract parameter 
             is not set and the entire option chain for a given symbol will be returned.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
             json returns the options data in JSON format; csv returns the data as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Realtime options data in JSON format or CSV string based on datatype parameter.


### Other

- **AD**: Returns the Chaikin A/D line (AD) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Chaikin A/D line values in the specified format.

- **ADD_TWO_NUMBERS**: Add two numbers together.
- **ADOSC**: Returns the Chaikin A/D oscillator (ADOSC) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    fastperiod: The time period of the fast EMA. Positive integers are accepted. By default, fastperiod=3.
    slowperiod: The time period of the slow EMA. Positive integers are accepted. By default, slowperiod=10.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Chaikin A/D oscillator values in the specified format.

- **ALUMINUM**: 
This API returns the global price of aluminum in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Aluminum price data in the specified format.

- **APO**: Returns the absolute price oscillator (APO) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastperiod: Positive integers are accepted. By default, fastperiod=12.
    slowperiod: Positive integers are accepted. By default, slowperiod=26.
    matype: Moving average type. By default, matype=0. Integers 0 - 8 are accepted with the following mappings.
           0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
           3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
           5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
           8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    APO values in the specified format (dict or str).

- **ATR**: Returns the average true range (ATR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each ATR value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The average true range (ATR) values in JSON or CSV format.

- **BOP**: Returns the balance of power (BOP) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Balance of power values in the specified format (dict or str).

- **CCI**: Returns the commodity channel index (CCI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each CCI value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Commodity channel index values in the specified format (dict or str).

- **CMO**: Returns the Chande momentum oscillator (CMO) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each CMO value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Chande momentum oscillator values in the specified format (dict or str).

- **COFFEE**: 
This API returns the global price of coffee in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Coffee price data in the specified format.

- **CORN**: 
This API returns the global price of corn in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Corn price data in the specified format.

- **COTTON**: 
This API returns the global price of cotton in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Cotton price data in the specified format.

- **CRYPTO_INTRADAY**: 
This API returns intraday time series (timestamp, open, high, low, close, volume) of the cryptocurrency specified, updated realtime.

Args:
    symbol: The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list. For example: symbol=ETH.
    market: The exchange market of your choice. It can be any of the market in the market list. For example: market=USD.
    interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
    outputsize: By default, outputsize=compact. Strings compact and full are accepted with the following specifications: compact returns only the latest 100 data points in the intraday time series; full returns the full-length intraday time series. The "compact" option is recommended if you would like to reduce the data size of each API call.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: json returns the intraday time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    The intraday time series data in the specified format.

- **DIVIDENDS**: Returns historical and future (declared) dividend distributions.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.
    datatype: By default, datatype=csv. Strings json and csv are accepted.
             json returns the data in JSON format; csv returns as CSV file.

Returns:
    Dividend data in specified format or error message.

- **DURABLES**: 
This API returns the monthly manufacturers' new orders of durable goods in the United States.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Durable goods orders time series data in JSON format or CSV string.

- **DX**: Returns the directional movement index (DX) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each DX value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The directional movement index (DX) values in JSON or CSV format.

- **ETF_PROFILE**: Returns key ETF metrics and holdings with allocation by asset types and sectors.

Includes net assets, expense ratio, turnover, and corresponding ETF holdings/constituents.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=QQQ.

Returns:
    ETF profile data in JSON format or error message.

- **FETCH**: 
Fetch complete financial data by calling the specified Alpha Vantage API function.

Args:
    id: Alpha Vantage API function name (from search results)

Returns:
    Complete data response with id, title, full data content, URL, and metadata

- **HT_DCPERIOD**: Returns the Hilbert transform, dominant cycle period (HT_DCPERIOD) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform dominant cycle period values in the specified format.

- **HT_DCPHASE**: Returns the Hilbert transform, dominant cycle phase (HT_DCPHASE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform dominant cycle phase values in the specified format.

- **HT_PHASOR**: Returns the Hilbert transform, phasor components (HT_PHASOR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform phasor components values in the specified format.

- **HT_SINE**: Returns the Hilbert transform, sine wave (HT_SINE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform sine wave values in the specified format.

- **HT_TRENDLINE**: Returns the Hilbert transform, instantaneous trendline (HT_TRENDLINE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform instantaneous trendline values in the specified format.

- **HT_TRENDMODE**: Returns the Hilbert transform, trend vs cycle mode (HT_TRENDMODE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Hilbert transform trend vs cycle mode values in the specified format.

- **MFI**: Returns the money flow index (MFI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MFI value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The money flow index (MFI) values in JSON or CSV format.

- **MIDPOINT**: Returns the midpoint (MIDPOINT) values. MIDPOINT = (highest value + lowest value)/2.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MIDPOINT value. Positive integers are accepted.
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The midpoint (MIDPOINT) values in JSON or CSV format.

- **MIDPRICE**: Returns the midpoint price (MIDPRICE) values. MIDPRICE = (highest high + lowest low)/2.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MIDPRICE value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The midpoint price (MIDPRICE) values in JSON or CSV format.

- **MINUS_DI**: Returns the minus directional indicator (MINUS_DI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MINUS_DI value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The minus directional indicator (MINUS_DI) values in JSON or CSV format.

- **MINUS_DM**: Returns the minus directional movement (MINUS_DM) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MINUS_DM value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The minus directional movement (MINUS_DM) values in JSON or CSV format.

- **NATR**: Returns the normalized average true range (NATR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each NATR value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The normalized average true range (NATR) values in JSON or CSV format.

- **NONFARM_PAYROLL**: 
This API returns the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, 
unpaid volunteers, farm employees, and the unincorporated self-employed.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Nonfarm payroll time series data in JSON format or CSV string.

- **OBV**: Returns the on balance volume (OBV) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. The daily/weekly/monthly intervals are agnostic to this parameter.
           By default, this parameter is not set and the technical indicator values will be calculated based on
           the most recent 30 days of intraday data. You can use the month parameter (in YYYY-MM format) to compute
           intraday technical indicators for a specific month in history. For example, month=2009-01.
           Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV
             (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The on balance volume values in the specified format.

- **PING**: Check if the service is healthy.
- **PLUS_DI**: Returns the plus directional indicator (PLUS_DI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each PLUS_DI value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The plus directional indicator (PLUS_DI) values in JSON or CSV format.

- **PLUS_DM**: Returns the plus directional movement (PLUS_DM) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each PLUS_DM value. Positive integers are accepted.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The plus directional movement (PLUS_DM) values in JSON or CSV format.

- **PPO**: Returns the percentage price oscillator (PPO) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastperiod: Positive integers are accepted. By default, fastperiod=12.
    slowperiod: Positive integers are accepted. By default, slowperiod=26.
    matype: Moving average type. By default, matype=0. Integers 0 - 8 are accepted with the following mappings.
           0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
           3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
           5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
           8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    PPO values in the specified format (dict or str).

- **RETAIL_SALES**: 
This API returns the monthly Advance Retail Sales: Retail Trade data of the United States.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Retail sales time series data in JSON format or CSV string.

- **ROC**: Returns the rate of change (ROC) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each ROC value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Rate of change values in the specified format (dict or str).

- **ROCR**: Returns the rate of change ratio (ROCR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each ROCR value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Rate of change ratio values in the specified format (dict or str).

- **SAR**: Returns the parabolic SAR (SAR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    acceleration: The acceleration factor. Positive floats are accepted. By default, acceleration=0.01.
    maximum: The acceleration factor maximum value. Positive floats are accepted. By default, maximum=0.20.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The parabolic SAR (SAR) values in JSON or CSV format.

- **SPLITS**: Returns historical split events.

Args:
    symbol: The symbol of the ticker of your choice. For example: symbol=IBM.
    datatype: By default, datatype=csv. Strings json and csv are accepted.
             json returns the data in JSON format; csv returns as CSV file.

Returns:
    Split data in specified format or error message.

- **SUGAR**: 
This API returns the global price of sugar in monthly, quarterly, and annual horizons.

Args:
    interval: By default, monthly. Strings monthly, quarterly, and annual are accepted.
    datatype: By default, csv. Strings json and csv are accepted with the following specifications:
             json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Sugar price data in the specified format.

- **T3**: 
Returns the triple exponential moving average (T3) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The T3 values in JSON or CSV format.

- **TRANGE**: Returns the true range (TRANGE) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The true range (TRANGE) values in JSON or CSV format.

- **TRIX**: Returns the 1-day rate of change of a triple smooth exponential moving average (TRIX) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each TRIX value. Positive integers are accepted.
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The 1-day rate of change of a triple smooth exponential moving average (TRIX) values in JSON or CSV format.

- **ULTOSC**: Returns the ultimate oscillator (ULTOSC) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    timeperiod1: The first time period for the indicator. Positive integers are accepted. By default, timeperiod1=7.
    timeperiod2: The second time period for the indicator. Positive integers are accepted. By default, timeperiod2=14.
    timeperiod3: The third time period for the indicator. Positive integers are accepted. By default, timeperiod3=28.
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The ultimate oscillator (ULTOSC) values in JSON or CSV format.

- **VWAP**: 
Returns the volume weighted average price (VWAP) for intraday time series.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             In keeping with mainstream investment literatures on VWAP, the following
             intraday intervals are supported: 1min, 5min, 15min, 30min, 60min
    month: By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The VWAP values in JSON or CSV format.

- **WILLR**: Returns the Williams' %R (WILLR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each WILLR value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Williams' %R values in the specified format (dict or str).


### Technical Indicators

- **ADX**: Returns the average directional movement index (ADX) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each ADX value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    ADX values in the specified format (dict or str).

- **ADXR**: Returns the average directional movement index rating (ADXR) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each ADXR value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    ADXR values in the specified format (dict or str).

- **AROON**: Returns the Aroon (AROON) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each AROON value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Aroon values in the specified format (dict or str).

- **AROONOSC**: Returns the Aroon oscillator (AROONOSC) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each AROONOSC value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Aroon oscillator values in the specified format (dict or str).

- **BBANDS**: Returns the Bollinger bands (BBANDS) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each BBANDS value. Positive integers are accepted.
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    nbdevup: The standard deviation multiplier of the upper band. Positive integers are accepted. By default, nbdevup=2.
    nbdevdn: The standard deviation multiplier of the lower band. Positive integers are accepted. By default, nbdevdn=2.
    matype: Moving average type of the time series. By default, matype=0. Integers 0-8 are accepted with the following mappings:
           0 = Simple Moving Average (SMA), 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
           3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
           5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
           8 = MESA Adaptive Moving Average (MAMA).
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
           for the equity markets. By default, this parameter is not set and the technical indicator values 
           will be calculated based on the most recent 30 days of intraday data. You can use the month 
           parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month 
           in history. For example, month=2009-01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The Bollinger bands (BBANDS) values in JSON or CSV format.

- **DEMA**: 
Returns the double exponential moving average (DEMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The DEMA values in JSON or CSV format.

- **EMA**: 
Returns the exponential moving average (EMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The EMA values in JSON or CSV format.

- **KAMA**: 
Returns the Kaufman adaptive moving average (KAMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The KAMA values in JSON or CSV format.

- **MACD**: 
Returns the moving average convergence / divergence (MACD) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastperiod: Positive integers are accepted. By default, fastperiod=12.
    slowperiod: Positive integers are accepted. By default, slowperiod=26.
    signalperiod: Positive integers are accepted. By default, signalperiod=9.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The MACD values in JSON or CSV format.

- **MACDEXT**: 
Returns the moving average convergence / divergence values with controllable moving average type.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastperiod: Positive integers are accepted. By default, fastperiod=12.
    slowperiod: Positive integers are accepted. By default, slowperiod=26.
    signalperiod: Positive integers are accepted. By default, signalperiod=9.
    fastmatype: Moving average type for the faster moving average. By default, fastmatype=0.
               Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
               1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
               3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
               5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
               8 = MESA Adaptive Moving Average (MAMA).
    slowmatype: Moving average type for the slower moving average. By default, slowmatype=0.
               Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
               1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
               3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
               5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
               8 = MESA Adaptive Moving Average (MAMA).
    signalmatype: Moving average type for the signal moving average. By default, signalmatype=0.
                 Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
                 1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
                 3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
                 5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
                 8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The MACDEXT values in JSON or CSV format.

- **MAMA**: 
Returns the MESA adaptive moving average (MAMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastlimit: Positive floats are accepted. By default, fastlimit=0.01.
    slowlimit: Positive floats are accepted. By default, slowlimit=0.01.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The MAMA values in JSON or CSV format.

- **MOM**: Returns the momentum (MOM) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each MOM value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    Momentum values in the specified format (dict or str).

- **RSI**: Returns the relative strength index (RSI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each RSI value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    RSI values in the specified format (dict or str).

- **SMA**: 
Returns the simple moving average (SMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The SMA values in JSON or CSV format.

- **STOCH**: 
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

- **STOCHF**: 
Returns the stochastic fast (STOCHF) values.

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
    fastdperiod: The time period of the fastd moving average. Positive integers are accepted. By default, fastdperiod=3.
    fastdmatype: Moving average type for the fastd moving average. By default, fastdmatype=0.
                Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
                1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
                3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
                5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
                8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The STOCHF values in JSON or CSV format.

- **STOCHRSI**: Returns the stochastic relative strength index (STOCHRSI) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each STOCHRSI value. Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min) for the equity markets.
          By default, this parameter is not set and the technical indicator values will be calculated based on the most recent 30 days of intraday data.
          You can use the month parameter (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    fastkperiod: The time period of the fastk moving average. Positive integers are accepted. By default, fastkperiod=5.
    fastdperiod: The time period of the fastd moving average. Positive integers are accepted. By default, fastdperiod=3.
    fastdmatype: Moving average type for the fastd moving average. By default, fastdmatype=0.
                Integers 0 - 8 are accepted with the following mappings. 0 = Simple Moving Average (SMA),
                1 = Exponential Moving Average (EMA), 2 = Weighted Moving Average (WMA),
                3 = Double Exponential Moving Average (DEMA), 4 = Triple Exponential Moving Average (TEMA),
                5 = Triangular Moving Average (TRIMA), 6 = T3 Moving Average, 7 = Kaufman Adaptive Moving Average (KAMA),
                8 = MESA Adaptive Moving Average (MAMA).
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV (comma separated value) file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    STOCHRSI values in the specified format (dict or str).

- **TEMA**: 
Returns the triple exponential moving average (TEMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The TEMA values in JSON or CSV format.

- **TRIMA**: 
Returns the triangular moving average (TRIMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The TRIMA values in JSON or CSV format.

- **WMA**: 
Returns the weighted moving average (WMA) values.

Args:
    symbol: The name of the ticker of your choice. For example: symbol=IBM
    interval: Time interval between two consecutive data points in the time series.
             The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    time_period: Number of data points used to calculate each moving average value.
                Positive integers are accepted (e.g., time_period=60, time_period=200)
    series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    month: Note: this parameter is ONLY applicable to intraday intervals (1min, 5min, 15min, 30min, and 60min)
          for the equity markets. By default, this parameter is not set and the technical indicator values will
          be calculated based on the most recent 30 days of intraday data. You can use the month parameter
          (in YYYY-MM format) to compute intraday technical indicators for a specific month in history.
          For example, month=2009-01. Any month equal to or later than 2000-01 (January 2000) is supported.
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications:
             json returns the daily time series in JSON format; csv returns the time series as a CSV file.


        entitlement: "delayed" for 15-minute delayed data, "realtime" for realtime data
Returns:
    The WMA values in JSON or CSV format.


## Usage Pattern

Each tool is a Python function that takes a dictionary of parameters:

```python
# Import the tool
from alphavantage import TIME_SERIES_DAILY

# Call with parameters
result = TIME_SERIES_DAILY({
    "symbol": "NVDA",
    "outputsize": "compact"
})

# Process the result
if "error" not in result:
    print(result)
else:
    print(f"Error: {result['error']}")
```

## Examples

### Get Daily Stock Data
```python
from alphavantage import TIME_SERIES_DAILY

data = TIME_SERIES_DAILY({"symbol": "AAPL"})
```

### Get Company Overview
```python
from alphavantage import COMPANY_OVERVIEW

overview = COMPANY_OVERVIEW({"symbol": "MSFT"})
```

### Search Symbols
```python
from alphavantage import SYMBOL_SEARCH

results = SYMBOL_SEARCH({"keywords": "tesla"})
```

## MCP Code Execution Pattern

This follows Anthropic's MCP code execution pattern:
- Tools are discovered by listing this directory
- Tool definitions are loaded on-demand
- Data processing happens in code before passing to the model
- Results can be filtered, aggregated, or transformed

See: https://www.anthropic.com/engineering/code-execution-with-mcp
