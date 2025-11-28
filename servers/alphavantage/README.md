# Alpha Vantage MCP Tools

This directory contains Python wrappers for all Alpha Vantage MCP tools.

## Available Tools (118 total)


### Alpha Intelligence

- **ANALYTICS_FIXED_WINDOW**: Returns advanced analytics metrics for time series over a fixed temporal window.
- **ANALYTICS_SLIDING_WINDOW**: Returns advanced analytics metrics for time series over sliding time windows.
- **EARNINGS**: Returns annual and quarterly earnings (EPS) for the company.
- **EARNINGS_CALENDAR**: Returns a list of company earnings expected in the next 3, 6, or 12 months.
- **EARNINGS_CALL_TRANSCRIPT**: Returns earnings call transcript for a company in a specific quarter.
- **EARNINGS_ESTIMATES**: Returns annual and quarterly EPS and revenue estimates with analyst data.
- **INSIDER_TRANSACTIONS**: Returns latest and historical insider transactions by key stakeholders.
- **NEWS_SENTIMENT**: Returns live and historical market news & sentiment data from premier news outlets worldwide.
- **TOP_GAINERS_LOSERS**: Returns top 20 gainers, losers, and most active traded tickers in the US market.

### Commodities

- **ALL_COMMODITIES**: This API returns the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.
- **BRENT**: This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.
- **COPPER**: This API returns the global price of copper in monthly, quarterly, and annual horizons.
- **NATURAL_GAS**: This API returns the Henry Hub natural gas spot prices in daily, weekly, and monthly horizons.
- **WHEAT**: This API returns the global price of wheat in monthly, quarterly, and annual horizons.
- **WTI**: This API returns the West Texas Intermediate (WTI) crude oil prices in daily, weekly, and monthly horizons.

### Core Stock APIs

- **GLOBAL_QUOTE**: Returns the latest price and volume information for a ticker.
- **MARKET_STATUS**: Returns the current market status (open vs. closed) of major trading venues worldwide.
- **REALTIME_BULK_QUOTES**: Returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per request.
- **SEARCH**: Search for relevant Alpha Vantage data based on natural language query.
- **SYMBOL_SEARCH**: Returns best-matching symbols and market information based on keywords.
- **TIME_SERIES_DAILY**: Returns raw daily time series (OHLCV) of the global equity specified, covering 20+ years of historical data.
- **TIME_SERIES_DAILY_ADJUSTED**: Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events.
- **TIME_SERIES_INTRADAY**: Returns current and 20+ years of historical intraday OHLCV time series of the equity specified.
- **TIME_SERIES_MONTHLY**: Returns monthly time series (last trading day of each month, OHLCV) covering 20+ years.
- **TIME_SERIES_MONTHLY_ADJUSTED**: Returns monthly adjusted time series (OHLCV, adjusted close, volume, dividend) covering 20+ years.
- **TIME_SERIES_WEEKLY**: Returns weekly time series (last trading day of each week, OHLCV) covering 20+ years of historical data.
- **TIME_SERIES_WEEKLY_ADJUSTED**: Returns weekly adjusted time series (OHLCV, adjusted close, volume, dividend) covering 20+ years.

### Cryptocurrencies

- **CURRENCY_EXCHANGE_RATE**: This API returns the realtime exchange rate for a pair of digital currency (e.g., Bitcoin) and physical currency (e.g., USD).
- **DIGITAL_CURRENCY_DAILY**: This API returns the daily historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.
- **DIGITAL_CURRENCY_MONTHLY**: This API returns the monthly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.
- **DIGITAL_CURRENCY_WEEKLY**: This API returns the weekly historical time series for a digital currency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

### Economic Indicators

- **CPI**: This API returns the monthly and semiannual consumer price index (CPI) of the United States. 
CPI is widely regarded as the barometer of inflation levels in the broader economy.
- **FEDERAL_FUNDS_RATE**: This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.
- **INFLATION**: This API returns the annual inflation rates (consumer prices) of the United States.
- **REAL_GDP**: This API returns the annual and quarterly Real GDP of the United States.
- **REAL_GDP_PER_CAPITA**: This API returns the quarterly Real GDP per Capita data of the United States.
- **TREASURY_YIELD**: This API returns the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).
- **UNEMPLOYMENT**: This API returns the monthly unemployment data of the United States. The unemployment rate represents the number of 
unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, 
who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions 
(e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces.

### Forex

- **FX_DAILY**: This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
- **FX_INTRADAY**: This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
- **FX_MONTHLY**: This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.
- **FX_WEEKLY**: This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.

### Fundamental Data

- **BALANCE_SHEET**: Returns annual and quarterly balance sheets with normalized fields.
- **CASH_FLOW**: Returns annual and quarterly cash flow with normalized fields.
- **COMPANY_OVERVIEW**: Returns company information, financial ratios, and key metrics for the specified equity.
- **INCOME_STATEMENT**: Returns annual and quarterly income statements with normalized fields.
- **IPO_CALENDAR**: Returns a list of IPOs expected in the next 3 months.
- **LISTING_STATUS**: Returns a list of active or delisted US stocks and ETFs.

### Options Data

- **HISTORICAL_OPTIONS**: Returns the full historical options chain for a specific symbol on a specific date.
- **REALTIME_OPTIONS**: Returns realtime US options data with full market coverage.

### Other

- **AD**: Returns the Chaikin A/D line (AD) values.
- **ADD_TWO_NUMBERS**: Add two numbers together.
- **ADOSC**: Returns the Chaikin A/D oscillator (ADOSC) values.
- **ALUMINUM**: This API returns the global price of aluminum in monthly, quarterly, and annual horizons.
- **APO**: Returns the absolute price oscillator (APO) values.
- **ATR**: Returns the average true range (ATR) values.
- **BOP**: Returns the balance of power (BOP) values.
- **CCI**: Returns the commodity channel index (CCI) values.
- **CMO**: Returns the Chande momentum oscillator (CMO) values.
- **COFFEE**: This API returns the global price of coffee in monthly, quarterly, and annual horizons.
- **CORN**: This API returns the global price of corn in monthly, quarterly, and annual horizons.
- **COTTON**: This API returns the global price of cotton in monthly, quarterly, and annual horizons.
- **CRYPTO_INTRADAY**: This API returns intraday time series (timestamp, open, high, low, close, volume) of the cryptocurrency specified, updated realtime.
- **DIVIDENDS**: Returns historical and future (declared) dividend distributions.
- **DURABLES**: This API returns the monthly manufacturers' new orders of durable goods in the United States.
- **DX**: Returns the directional movement index (DX) values.
- **ETF_PROFILE**: Returns key ETF metrics and holdings with allocation by asset types and sectors.
- **FETCH**: Fetch complete financial data by calling the specified Alpha Vantage API function.
- **HT_DCPERIOD**: Returns the Hilbert transform, dominant cycle period (HT_DCPERIOD) values.
- **HT_DCPHASE**: Returns the Hilbert transform, dominant cycle phase (HT_DCPHASE) values.
- **HT_PHASOR**: Returns the Hilbert transform, phasor components (HT_PHASOR) values.
- **HT_SINE**: Returns the Hilbert transform, sine wave (HT_SINE) values.
- **HT_TRENDLINE**: Returns the Hilbert transform, instantaneous trendline (HT_TRENDLINE) values.
- **HT_TRENDMODE**: Returns the Hilbert transform, trend vs cycle mode (HT_TRENDMODE) values.
- **MFI**: Returns the money flow index (MFI) values.
- **MIDPOINT**: Returns the midpoint (MIDPOINT) values. MIDPOINT = (highest value + lowest value)/2.
- **MIDPRICE**: Returns the midpoint price (MIDPRICE) values. MIDPRICE = (highest high + lowest low)/2.
- **MINUS_DI**: Returns the minus directional indicator (MINUS_DI) values.
- **MINUS_DM**: Returns the minus directional movement (MINUS_DM) values.
- **NATR**: Returns the normalized average true range (NATR) values.
- **NONFARM_PAYROLL**: This API returns the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, 
unpaid volunteers, farm employees, and the unincorporated self-employed.
- **OBV**: Returns the on balance volume (OBV) values.
- **PING**: Check if the service is healthy.
- **PLUS_DI**: Returns the plus directional indicator (PLUS_DI) values.
- **PLUS_DM**: Returns the plus directional movement (PLUS_DM) values.
- **PPO**: Returns the percentage price oscillator (PPO) values.
- **RETAIL_SALES**: This API returns the monthly Advance Retail Sales: Retail Trade data of the United States.
- **ROC**: Returns the rate of change (ROC) values.
- **ROCR**: Returns the rate of change ratio (ROCR) values.
- **SAR**: Returns the parabolic SAR (SAR) values.
- **SPLITS**: Returns historical split events.
- **SUGAR**: This API returns the global price of sugar in monthly, quarterly, and annual horizons.
- **T3**: Returns the triple exponential moving average (T3) values.
- **TRANGE**: Returns the true range (TRANGE) values.
- **TRIX**: Returns the 1-day rate of change of a triple smooth exponential moving average (TRIX) values.
- **ULTOSC**: Returns the ultimate oscillator (ULTOSC) values.
- **VWAP**: Returns the volume weighted average price (VWAP) for intraday time series.
- **WILLR**: Returns the Williams' %R (WILLR) values.

### Technical Indicators

- **ADX**: Returns the average directional movement index (ADX) values.
- **ADXR**: Returns the average directional movement index rating (ADXR) values.
- **AROON**: Returns the Aroon (AROON) values.
- **AROONOSC**: Returns the Aroon oscillator (AROONOSC) values.
- **BBANDS**: Returns the Bollinger bands (BBANDS) values.
- **DEMA**: Returns the double exponential moving average (DEMA) values.
- **EMA**: Returns the exponential moving average (EMA) values.
- **KAMA**: Returns the Kaufman adaptive moving average (KAMA) values.
- **MACD**: Returns the moving average convergence / divergence (MACD) values.
- **MACDEXT**: Returns the moving average convergence / divergence values with controllable moving average type.
- **MAMA**: Returns the MESA adaptive moving average (MAMA) values.
- **MOM**: Returns the momentum (MOM) values.
- **RSI**: Returns the relative strength index (RSI) values.
- **SMA**: Returns the simple moving average (SMA) values.
- **STOCH**: Returns the stochastic oscillator (STOCH) values.
- **STOCHF**: Returns the stochastic fast (STOCHF) values.
- **STOCHRSI**: Returns the stochastic relative strength index (STOCHRSI) values.
- **TEMA**: Returns the triple exponential moving average (TEMA) values.
- **TRIMA**: Returns the triangular moving average (TRIMA) values.
- **WMA**: Returns the weighted moving average (WMA) values.

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
