# MCP Agent with Alpha Vantage Integration

A command-line AI agent that follows [Anthropic's MCP code execution pattern](https://www.anthropic.com/engineering/code-execution-with-mcp) and integrates with [Alpha Vantage's MCP server](https://mcp.alphavantage.co/) for financial data analysis.

## Architecture

This agent implements the **progressive disclosure** pattern described in Anthropic's article:

```
agent.py                     # Main CLI agent
├── servers/
│   ├── mcp_client.py       # MCP protocol client
│   ├── generate_tools.py   # Tool generator
│   └── alphavantage/       # Generated tool files
│       ├── __init__.py
│       ├── README.md
│       ├── TIME_SERIES_DAILY.py
│       ├── GLOBAL_QUOTE.py
│       └── ... (100+ tools)
├── workspace/              # Agent workspace for files
└── skills/                 # Reusable code patterns
```

### Key Design Principles

1. **Progressive Disclosure**: Tools are discovered by listing the filesystem, not loaded upfront
2. **Context Efficiency**: Data processing happens in code before passing to the model
3. **State Persistence**: Intermediate results saved to workspace
4. **Reusable Skills**: Successful patterns can be saved for future use

## Setup

### 1. Install Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt
```

### 2. Set API Keys

You'll need two API keys:

```bash
# Anthropic API key (required for the agent)
export ANTHROPIC_API_KEY='your-anthropic-api-key'

# Alpha Vantage API key (required for financial data)
# Get your free key at: https://www.alphavantage.co/support/#api-key
export ALPHA_VANTAGE_API_KEY='your-alphavantage-api-key'
```

### 3. Generate Tool Files

This fetches all available tools from the Alpha Vantage MCP server and creates Python wrapper files:

```bash
python servers/generate_tools.py
```

You should see output like:
```
Fetching tools from Alpha Vantage MCP server...
Found 120 tools

Generating tool files...
  - TIME_SERIES_INTRADAY
  - TIME_SERIES_DAILY
  - GLOBAL_QUOTE
  ...

✓ Successfully generated 120 tool files in /home/claude/servers/alphavantage
```

### 4. Run the Agent

```bash
python agent_multi_stage.py
```

## Usage Examples

### Example 1: Discover Available Tools

```
You: What tools are available?

Agent: [Lists directories in servers/]
[Reads alphavantage/README.md]

I can see the Alpha Vantage server has 120+ tools organized into:
- Core Stock APIs (TIME_SERIES_DAILY, GLOBAL_QUOTE, etc.)
- Options Data
- Alpha Intelligence (news, earnings, insider transactions)
- Fundamental Data (income statements, balance sheets)
- Forex, Cryptocurrencies, Commodities
- Economic Indicators
- Technical Indicators
...
```

### Example 2: Get Stock Price

```
You: What's the current price of NVIDIA stock?

Agent: [Tool: list_directory]
[Tool: read_file - servers/alphavantage/GLOBAL_QUOTE.py]
[Tool: execute_code]

from servers.alphavantage.GLOBAL_QUOTE import GLOBAL_QUOTE
result = GLOBAL_QUOTE({"symbol": "NVDA"})
print(result)

Output:
{
  "Global Quote": {
    "01. symbol": "NVDA",
    "05. price": "145.67",
    "09. change": "+2.34",
    ...
  }
}

NVIDIA (NVDA) is currently trading at $145.67, up $2.34 today.
```

### Example 3: Analyze Multiple Stocks

```
You: Compare the daily performance of NVDA, AMD, and INTC over the past week

Agent: [Loads TIME_SERIES_DAILY tool]
[Executes code to fetch all three stocks]
[Filters to last 5 trading days]
[Calculates percentage changes]
[Creates comparison table]

Here's the performance comparison:

| Symbol | Week Change | Mon | Tue | Wed | Thu | Fri |
|--------|-------------|-----|-----|-----|-----|-----|
| NVDA   | +8.2%       | ... | ... | ... | ... | ... |
| AMD    | +5.1%       | ... | ... | ... | ... | ... |
| INTC   | -1.3%       | ... | ... | ... | ... | ... |

NVIDIA led the group with strong gains...
```

### Example 4: Save Analysis as Skill

```
You: Save that stock comparison code as a reusable skill

Agent: [Saves code to skills/compare_stocks.py]
[Creates SKILL.md documentation]

I've saved the stock comparison logic to skills/compare_stocks.py.
You can now reuse it with:

from skills.compare_stocks import compare_stocks
result = compare_stocks(["NVDA", "AMD", "INTC"])
```

## How It Works

### Progressive Tool Discovery

Instead of loading all 120+ tool definitions upfront (which would use ~150,000 tokens), the agent:

1. Lists the `servers/` directory to find available servers
2. Reads only the specific tool files it needs
3. Executes code to call those tools
4. Processes results before showing them to you

This reduces token usage by **~98%** compared to traditional MCP clients.

### Code Execution Pattern

When you ask about stock prices, the agent:

```python
# 1. Discovers the tool
os.listdir('servers/alphavantage/')  # See available tools

# 2. Loads only what's needed
with open('servers/alphavantage/GLOBAL_QUOTE.py') as f:
    tool_def = f.read()

# 3. Executes in code
from servers.alphavantage.GLOBAL_QUOTE import GLOBAL_QUOTE
result = GLOBAL_QUOTE({"symbol": "NVDA"})

# 4. Processes before returning
price = result["Global Quote"]["05. price"]
print(f"Current price: ${price}")  # Only this goes to model
```

### Privacy and Security

- Intermediate data stays in the code execution environment
- Only explicitly logged results go to the model
- Sensitive data can flow between tools without entering the model's context

## Available Tool Categories

### Core Stock APIs
- Intraday, daily, weekly, monthly time series
- Real-time quotes and bulk quotes
- Symbol search and market status

### Options Data
- Real-time options with Greeks
- Historical options chains (15+ years)

### Alpha Intelligence
- News sentiment analysis
- Earnings call transcripts
- Top gainers/losers
- Insider transactions
- Advanced analytics

### Fundamental Data
- Company overviews
- Income statements, balance sheets, cash flow
- Earnings data and calendars
- IPO calendar

### Forex, Crypto, Commodities
- Currency exchange rates
- Digital currency data
- Commodities prices (oil, gold, wheat, etc.)

### Economic Indicators
- GDP, unemployment, inflation
- Treasury yields, Federal funds rate
- Retail sales, durable goods

### Technical Indicators
- Moving averages (SMA, EMA, VWAP, etc.)
- Oscillators (RSI, MACD, Stochastic)
- Bollinger Bands, ATR, and more

## Architecture Benefits

### vs. Traditional MCP Client

| Aspect | Traditional | Code Execution Pattern |
|--------|-------------|------------------------|
| Tool definitions | All loaded upfront | Loaded on-demand |
| Context usage | 150,000+ tokens | 2,000 tokens (-98.7%) |
| Data processing | Through model context | In execution environment |
| Large datasets | May exceed limits | Filtered before model |
| State management | Lost between calls | Persisted to filesystem |

### When to Use This Pattern

✅ **Good for:**
- Many tools available (100+)
- Large data processing
- Multi-step workflows
- Privacy-sensitive data
- Building reusable skills

❌ **Overkill for:**
- Few tools (< 10)
- Simple single-call operations
- No data processing needed

## Extending the Agent

### Add More MCP Servers

Create a new directory in `servers/`:

```bash
servers/
├── alphavantage/
├── your_new_server/
│   ├── tool1.py
│   ├── tool2.py
│   └── __init__.py
```

The agent will automatically discover it.

### Create Custom Skills

Save reusable code patterns to `skills/`:

```python
# skills/my_analysis.py
def my_custom_analysis(symbol):
    # Your code here
    pass
```

Add a `SKILL.md` file to document it.

### Modify the Agent

Edit `agent.py` to:
- Add new tools (file operations, databases, etc.)
- Change the model or parameters
- Customize the system prompt
- Add safety constraints

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### "ALPHA_VANTAGE_API_KEY not set"
```bash
export ALPHA_VANTAGE_API_KEY='your-key-here'
# Get free key at: https://www.alphavantage.co/support/#api-key
```

### "No tools generated"
- Check your Alpha Vantage API key is valid
- Ensure you have internet connectivity
- Try running `generate_tools.py` again

### Rate Limiting
Alpha Vantage has rate limits:
- Free tier: 25 requests/day
- Premium tiers: Higher limits

The agent will show rate limit errors in tool results.

## References

- [Anthropic MCP Code Execution Article](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [Alpha Vantage MCP Server](https://mcp.alphavantage.co/)
- [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- [Alpha Vantage API Docs](https://www.alphavantage.co/documentation/)

## License

MIT License - Feel free to modify and extend this agent for your needs.
