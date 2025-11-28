#!/usr/bin/env python3
"""
Generate Python tool files from Alpha Vantage MCP server.
This creates a file for each tool following the code execution pattern.
"""

import sys
import os
from pathlib import Path

from mcp_client import list_available_tools, ALPHA_VANTAGE_API_KEY

ALPHAVANTAGE_DIR = Path("alphavantage")


def generate_tool_file(tool: dict) -> str:
    """Generate Python code for a single tool."""
    
    tool_name = tool.get("name", "unknown")
    description = tool.get("description", "No description available")
    input_schema = tool.get("inputSchema", {})
    
    # Extract parameters
    properties = input_schema.get("properties", {})
    required = input_schema.get("required", [])
    
    # Generate parameter documentation
    param_docs = []
    for param_name, param_info in properties.items():
        param_type = param_info.get("type", "any")
        param_desc = param_info.get("description", "")
        is_required = "required" if param_name in required else "optional"
        param_docs.append(f"            {param_name} ({is_required}, {param_type}): {param_desc}")

    params_doc = "\n".join(param_docs) if param_docs else "            No parameters required"

    code = f'''
from servers.mcp_client import call_mcp_tool


def {tool_name}(params: dict = None) -> dict:
    """
    {description}

    Args:
        params (dict, optional): Dictionary containing the following parameters:
{params_doc}

    Returns:
        dict: API response containing the requested data or error information
    """
    if params is None:
        params = {{}}
    return call_mcp_tool("{tool_name}", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing {tool_name}...")
    result = {tool_name}()
    print(json.dumps(result, indent=2))
'''
    
    return code


def generate_index_file(tools: list) -> str:
    """Generate __init__.py that exports all tools."""
    
    imports = []
    exports = []
    
    for tool in tools:
        tool_name = tool.get("name", "unknown")
        imports.append(f"from .{tool_name} import {tool_name}")
        exports.append(f'    "{tool_name}",')
    
    code = f'''"""
Alpha Vantage MCP Tools
All available financial data tools from Alpha Vantage.

Usage:
    from alphavantage import TIME_SERIES_DAILY
    result = TIME_SERIES_DAILY({{"symbol": "NVDA"}})
"""

{chr(10).join(imports)}

__all__ = [
{chr(10).join(exports)}
]
'''
    
    return code


def generate_readme(tools: list) -> str:
    """Generate README with tool documentation."""
    
    # Group tools by category
    categories = {}
    for tool in tools:
        tool_name = tool.get("name", "unknown")
        description = tool.get("description", "")
        
        # Infer category from tool name
        if any(x in tool_name for x in ["TIME_SERIES", "QUOTE", "SEARCH", "MARKET"]):
            category = "Core Stock APIs"
        elif "OPTIONS" in tool_name:
            category = "Options Data"
        elif any(x in tool_name for x in ["NEWS", "EARNINGS", "GAINERS", "INSIDER", "ANALYTICS"]):
            category = "Alpha Intelligence"
        elif any(x in tool_name for x in ["COMPANY", "INCOME", "BALANCE", "CASH", "LISTING", "IPO"]):
            category = "Fundamental Data"
        elif "FX" in tool_name:
            category = "Forex"
        elif any(x in tool_name for x in ["CURRENCY", "DIGITAL"]):
            category = "Cryptocurrencies"
        elif any(x in tool_name for x in ["WTI", "BRENT", "GAS", "COPPER", "WHEAT", "COMMODITIES"]):
            category = "Commodities"
        elif any(x in tool_name for x in ["GDP", "TREASURY", "FEDERAL", "CPI", "INFLATION", "UNEMPLOYMENT"]):
            category = "Economic Indicators"
        elif tool_name in ["SMA", "EMA", "MACD", "RSI", "BBANDS"] or any(x in tool_name for x in ["MA", "STOCH", "ADX", "MOM", "AROON"]):
            category = "Technical Indicators"
        else:
            category = "Other"
        
        if category not in categories:
            categories[category] = []
        categories[category].append((tool_name, description))
    
    # Generate markdown
    readme = f"""# Alpha Vantage MCP Tools

This directory contains Python wrappers for all Alpha Vantage MCP tools.

## Available Tools ({len(tools)} total)

"""
    
    for category in sorted(categories.keys()):
        readme += f"\n### {category}\n\n"
        for tool_name, description in sorted(categories[category]):
            readme += f"- **{tool_name}**: {description}\n"
    
    readme += """
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
"""
    
    return readme


def main():
    """Generate all tool files."""
    
    if not ALPHA_VANTAGE_API_KEY:
        print("Error: ALPHA_VANTAGE_API_KEY environment variable not set")
        print("Please create a .env file with:")
        print("ALPHA_VANTAGE_API_KEY=your-key-here")
        sys.exit(1)
    
    print("Fetching tools from Alpha Vantage MCP server...")
    tools = list_available_tools()
    
    if not tools or "error" in tools[0]:
        print(f"Error fetching tools: {tools}")
        sys.exit(1)
    
    print(f"✓ Found {len(tools)} tools")
    
    # Create alphavantage directory
    ALPHAVANTAGE_DIR.mkdir(exist_ok=True)
    print(f"✓ Created {ALPHAVANTAGE_DIR}/ directory")
    
    # Generate individual tool files
    print("\nGenerating tool files...")
    for i, tool in enumerate(tools, 1):
        tool_name = tool.get("name", "unknown")
        print(f"  [{i}/{len(tools)}] {tool_name}")
        
        code = generate_tool_file(tool)
        file_path = ALPHAVANTAGE_DIR / f"{tool_name}.py"
        
        with open(file_path, 'w') as f:
            f.write(code)
    
    # Generate __init__.py for the package
    init_file = ALPHAVANTAGE_DIR / "__init__.py"
    with open(init_file, 'w') as f:
        f.write(generate_index_file(tools))
    print(f"\n✓ Generated {init_file}")
    
    # Generate README
    readme_file = ALPHAVANTAGE_DIR / "README.md"
    with open(readme_file, 'w') as f:
        f.write(generate_readme(tools))
    print(f"✓ Generated {readme_file}")
    
    print(f"\n{'='*60}")
    print(f"✓ Successfully generated {len(tools)} tool files!")
    print(f"{'='*60}")
    print("\nNext steps:")
    print("1. Try using a tool:")
    print("   python -c 'from alphavantage import TIME_SERIES_DAILY; import json; print(json.dumps(TIME_SERIES_DAILY({\"symbol\": \"NVDA\"}), indent=2))'")
    print("\n2. Or build your agent using these tools!")


if __name__ == "__main__":
    main()
