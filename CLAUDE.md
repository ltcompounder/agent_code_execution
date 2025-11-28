# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a multi-agent financial data analysis system implementing Anthropic's MCP code execution pattern with Alpha Vantage integration. The architecture uses **progressive disclosure** - tools are discovered on-demand rather than loaded upfront, achieving ~98% reduction in token usage.

## Essential Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Set required environment variables
export ANTHROPIC_API_KEY='your-anthropic-api-key'
export ALPHA_VANTAGE_API_KEY='your-alphavantage-api-key'

# Generate tool files from Alpha Vantage MCP server
python servers/generate_tools.py
```

### Running the Agent
```bash
# Run the multi-agent pipeline
python agent_multi_stage.py
```

### Testing MCP Connection
```bash
# Test MCP client connection
python servers/mcp_client.py

# Test individual tool
python -c 'from servers.alphavantage import GLOBAL_QUOTE; import json; print(json.dumps(GLOBAL_QUOTE({"symbol": "NVDA"}), indent=2))'
```

## Architecture

### 5-Agent Pipeline

The system orchestrates 5 specialized agents in `agent_multi_stage.py`:

1. **Explorer (Discovery)** - Scans `servers/alphavantage/` filesystem to discover all available tools
2. **Explorer (Selection)** - Analyzes user query and selects the best-matching tool from discovered list
3. **Reader** - Reads the selected tool file and extracts its interface (parameters, types, descriptions)
4. **Coder** - Generates executable Python code that calls the tool with appropriate parameters
5. **Executor** - Runs the generated code and captures API response
6. **Parser** - Formats raw API response into natural language answer

Each agent uses `call_agent()` which creates a fresh Claude API call with a specialized system prompt.

### Progressive Disclosure Pattern

**Key principle**: Don't load all 118+ tool definitions upfront. Instead:

- Tools are Python files in `servers/alphavantage/`
- Discovery agent lists directory to find available tools
- Only the selected tool file is read
- Code executes and processes data before returning to model
- Intermediate results can be filtered/transformed in execution environment

This keeps context usage minimal (~2,000 tokens vs ~150,000 tokens).

### MCP Integration

**File**: `servers/mcp_client.py`

Provides synchronous and async functions for Alpha Vantage MCP server:
- `list_available_tools()` - Fetches all tools from MCP server
- `call_mcp_tool(tool_name, arguments)` - Calls specific tool with parameters
- Uses JSON-RPC protocol over HTTPS to `https://mcp.alphavantage.co`

**File**: `servers/generate_tools.py`

Generates Python wrapper files for each MCP tool:
- Fetches tool list from MCP server
- Creates individual `.py` files in `servers/alphavantage/`
- Each tool file imports `call_mcp_tool()` from `mcp_client.py`
- Generates `__init__.py` for package imports
- Creates categorized README.md

### Tool Structure

Generated tools in `servers/alphavantage/` follow this pattern:

```python
from servers.mcp_client import call_mcp_tool

def TOOL_NAME(params: dict = None) -> dict:
    """
    Description from MCP server

    Args:
        params (dict, optional): Dictionary containing:
            parameter_name (required/optional, type): Description

    Returns:
        dict: API response or error information
    """
    if params is None:
        params = {}
    return call_mcp_tool("TOOL_NAME", params)
```

## Important Implementation Details

### Parameter Format Handling

**CRITICAL**: The Coder agent must extract parameter formats from tool documentation examples and use them exactly as shown. Common format patterns:

- Quarterly data: `"2025Q3"` (not `"202503"` or `"2025-Q3"`)
- Dates: `"YYYY-MM-DD"` format when specified
- Tool documentation contains format examples - follow them literally

### Code Execution

**Function**: `execute_python_code(code, working_dir)`
- Creates temporary Python file
- Executes via subprocess with 30-second timeout
- Returns dict with `stdout`, `stderr`, `returncode`, `success`
- Cleans up temp file after execution

### Tool Selection Logic

The Explorer (Selection) agent uses keyword matching with priority:
1. Exact phrase match (e.g., "earnings transcript" → `EARNINGS_CALL_TRANSCRIPT`)
2. Specific distinguishing keywords (e.g., "transcript" must appear in tool name)
3. General category match

Pay attention to similar tool names:
- `EARNINGS` vs `EARNINGS_CALL_TRANSCRIPT` vs `EARNINGS_CALENDAR` vs `EARNINGS_ESTIMATES`
- `GLOBAL_QUOTE` (current) vs `TIME_SERIES_DAILY` (historical)

### Error Handling

- All agents use try/except blocks
- API errors are returned as JSON: `{"error": "message"}`
- Parser agent formats errors in user-friendly language
- Rate limiting errors from Alpha Vantage should be explained to user

## Tool Categories

118 total tools organized into:

- **Core Stock APIs**: TIME_SERIES_*, GLOBAL_QUOTE, SYMBOL_SEARCH, MARKET_STATUS
- **Options Data**: REALTIME_OPTIONS, HISTORICAL_OPTIONS
- **Alpha Intelligence**: NEWS_SENTIMENT, EARNINGS_CALL_TRANSCRIPT, TOP_GAINERS_LOSERS, INSIDER_TRANSACTIONS, ANALYTICS_*
- **Fundamental Data**: COMPANY_OVERVIEW, INCOME_STATEMENT, BALANCE_SHEET, CASH_FLOW, IPO_CALENDAR
- **Forex**: FX_DAILY, FX_INTRADAY, FX_WEEKLY, FX_MONTHLY
- **Cryptocurrencies**: DIGITAL_CURRENCY_*, CURRENCY_EXCHANGE_RATE, CRYPTO_INTRADAY
- **Commodities**: WTI, BRENT, NATURAL_GAS, COPPER, WHEAT, CORN, etc.
- **Economic Indicators**: REAL_GDP, UNEMPLOYMENT, INFLATION, CPI, TREASURY_YIELD, FEDERAL_FUNDS_RATE
- **Technical Indicators**: SMA, EMA, MACD, RSI, BBANDS, STOCH, ADX, etc.

See `servers/alphavantage/README.md` for complete categorized list.

## Dependencies

From `requirements.txt`:
- `anthropic>=0.39.0` - Claude API client
- `requests>=2.31.0` - HTTP requests
- `mcp>=1.21.1` - Model Context Protocol
- `python-dotenv>=1.2.1` - Environment variable loading

Also uses `httpx` (async HTTP client) in `mcp_client.py`.

## Extending the System

### Adding New MCP Servers

Create new directory in `servers/` with tool files following the same pattern. The Explorer agent will automatically discover them via filesystem listing.

### Modifying Agent Behavior

Each agent's behavior is controlled by its system prompt constant in `agent_multi_stage.py`:
- `EXPLORER_DISCOVERY_PROMPT`
- `EXPLORER_SELECTION_PROMPT`
- `READER_PROMPT`
- `CODER_PROMPT`
- `PARSER_PROMPT`

### Model Selection

Default model is `claude-sonnet-4-20250514` specified in `call_agent()`. Change this parameter to use different models.

## Design Principles

1. **Progressive Disclosure**: Discover tools on-demand, not upfront
2. **Context Efficiency**: Process data in code execution environment before passing to model
3. **State Persistence**: Results can be saved to filesystem (workspace/) for multi-step workflows
4. **Reusable Patterns**: Successful code patterns can be saved as skills (skills/ directory)
5. **Privacy**: Sensitive data flows through code execution without entering model context

## Common Patterns

### User Query Flow
```
User: "What's NVIDIA's current price?"
  ↓
Explorer Discovery: List all tools in servers/alphavantage/
  ↓
Explorer Selection: Choose GLOBAL_QUOTE based on "current price" keywords
  ↓
Reader: Read GLOBAL_QUOTE.py and extract parameters (symbol required)
  ↓
Coder: Generate code: GLOBAL_QUOTE({"symbol": "NVDA"})
  ↓
Executor: Run code, get JSON response
  ↓
Parser: Format as "NVIDIA (NVDA) is currently trading at $X.XX..."
```

### Adding New Tool Files
```bash
# After modifying MCP server or getting new API key
python servers/generate_tools.py
```

This regenerates all tool files from the current MCP server state.
