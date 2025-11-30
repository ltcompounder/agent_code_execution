#!/usr/bin/env python3
"""
5-Agent MCP Code Execution Pipeline
Explorer (Discovery) → Explorer (Selection) → Reader → Coder → Executor → Parser
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed")
    print("Install with: pip install anthropic")
    sys.exit(1)

# Initialize Anthropic client
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not ANTHROPIC_API_KEY and __name__ == "__main__":
    print("Error: ANTHROPIC_API_KEY not set in .env file")
    sys.exit(1)

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None

# Working directory
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
# AGENT 1A: EXPLORER - DISCOVERY (Find all available tools)
# ============================================================================

EXPLORER_DISCOVERY_PROMPT = """You are a tool discovery agent.

Your task: Scan the alphavantage tools directory to find all available tools.

Write and execute code to discover all available tools:

```python
import os

try:
    # Use absolute path based on this file's location (works in serverless environments)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tools_dir = os.path.join(script_dir, 'servers', 'alphavantage')

    # List all files
    all_files = os.listdir(tools_dir)

    # Filter for Python tool files
    tool_files = [f for f in all_files if f.endswith('.py') and f != '__init__.py']

    # Remove .py extension and sort
    tools = sorted([f[:-3] for f in tool_files])

    # Print results
    print("Available tools: " + str(len(tools)) + " total")
    for tool in tools:
        print("  - " + tool)

except Exception as e:
    print("Error discovering tools: " + str(e))
    import traceback
    traceback.print_exc()
```

Execute this code to discover all available tools.
"""

# ============================================================================
# AGENT 1B: EXPLORER - SELECTION (Select best tool for query)
# ============================================================================

EXPLORER_SELECTION_PROMPT = """You are a tool selection agent.

Your task: Select the most appropriate tool for the user's query from the available tools.

User query: {user_query}

Available tools:
{available_tools}

SELECTION RULES:
1. Match keywords in the user query to tool names
2. Pay close attention to specific words that distinguish similar tools
3. If user mentions a specific word (like "transcript"), prioritize tools with that exact word

IMPORTANT DISTINCTIONS:
- "earnings transcript" or "earnings call" → EARNINGS_CALL_TRANSCRIPT (not EARNINGS!)
- "earnings calendar" → EARNINGS_CALENDAR
- "earnings estimates" → EARNINGS_ESTIMATES
- "earnings" alone (without transcript/call/calendar) → EARNINGS

- "current price" or "quote" → GLOBAL_QUOTE
- "historical prices" or "time series" → TIME_SERIES_DAILY
- "intraday" → TIME_SERIES_INTRADAY

- "company overview" or "company info" → COMPANY_OVERVIEW
- "news" or "sentiment" → NEWS_SENTIMENT
- "symbol search" or "ticker search" → SYMBOL_SEARCH

KEYWORD MATCHING PRIORITY:
1. Exact phrase match (e.g., "earnings transcript" → look for tool with both words)
2. Specific distinguishing keywords (e.g., "transcript" → must have TRANSCRIPT in name)
3. General category match

Analyze the user query carefully and select the single most appropriate tool.

Output format (just one line):
SELECTED_TOOL: [exact tool name]
"""

# ============================================================================
# AGENT 2: READER (Understanding)
# ============================================================================

READER_PROMPT = """You are a tool reader agent.

Your task: Analyze the tool file content and extract its complete interface.

Tool: {tool_name}

File content:
{tool_content}

Carefully analyze the docstring and extract parameters:

IMPORTANT: Look for the "Args:" section in the docstring. Parameters are listed like:
    symbol (required, string): Description here
    quarter (required, string): Description here
    datatype (optional, string): Description here

Pay attention to whether each parameter is marked as "required" or "optional".

Extract and output in this EXACT format:

TOOL: {tool_name}
DESCRIPTION: [one-line summary - first line of docstring]
PARAMETERS:
  - parameter_name (REQUIRED/OPTIONAL, type): Description with examples
  - parameter_name (REQUIRED/OPTIONAL, type): Description with examples
EXAMPLE_CALL: {tool_name}({{"param1": "value1", "param2": "value2"}})

Be thorough - list ALL parameters you find in the Args section with their exact descriptions including any format examples.
"""

# ============================================================================
# AGENT 3: CODER (Code Generation)
# ============================================================================

CODER_PROMPT = """You are a code generation agent.

Your task: Generate Python code to answer the user's query using the specified tool.

User query: {user_query}
Tool: {tool_name}
Tool interface:
{tool_interface}

CRITICAL RULES FOR PARAMETER VALUES:
1. Read the parameter descriptions carefully - they contain EXAMPLES of the exact format to use
2. If a parameter has an example like "Example: 2024Q1", use THAT EXACT FORMAT
3. Do NOT convert or reformat values - use the documented format exactly as shown
4. Pay attention to format examples:
   - "YYYYQM format. Example: 2024Q1" means use "2025Q3" NOT "202503" or "2025-Q3"
   - "YYYY-MM-DD format" means use "2025-01-15" NOT "20250115"
   - Follow the literal example format shown

PARAMETER EXTRACTION FROM USER QUERY:
- Extract values from user query: "Q3 2025" → convert to documented format: "2025Q3"
- "third quarter 2025" → "2025Q3"
- "January 2025" → depends on format requirement (check documentation)

Generate clean Python code that:
1. Imports from servers.alphavantage
2. Calls the tool with parameters in the EXACT format shown in documentation examples
3. Handles the response appropriately
4. Prints the RAW result as JSON (this will be parsed by the Parser Agent)

Guidelines:
- Wrap code in ```python blocks
- Use try/except for error handling
- Output MUST be valid JSON that can be parsed
- Use json.dumps() to ensure clean JSON output
- Include comments showing parameter format

Example structure:
```python
import json
from servers.alphavantage import {tool_name}

try:
    # Call the tool with parameters in correct format
    result = {tool_name}({{"param": "value"}})  # Use format from documentation!

    # Output raw result as JSON for Parser Agent
    print(json.dumps(result, indent=2))

except Exception as e:
    # Output error as JSON
    print(json.dumps({{"error": str(e)}}))
```

Generate ONLY the code block, minimal explanation.
"""

# ============================================================================
# AGENT 4: PARSER (Response Formatting)
# ============================================================================

PARSER_PROMPT = """You are a response parsing and formatting agent.

Your task: Convert raw API response data into a natural, human-readable answer to the user's query.

User query: {user_query}
Tool used: {tool_name}
Raw API response:
{api_response}

PARSING RULES:
1. Extract ONLY the information relevant to the user's query
2. Format the response in clear, natural language
3. If there's an error, explain it in user-friendly terms
4. Include relevant numbers, dates, and metrics
5. Use bullet points or structured format when appropriate
6. Keep it concise but informative

COMMON SCENARIOS:

Stock Price Queries:
- Extract: current price, change, volume, timestamp
- Format: "Tesla (TSLA) is currently trading at $245.67, up $3.45 (+1.43%) with volume of 125.4M shares."

Company Overview:
- Extract: company name, sector, industry, description, market cap, PE ratio
- Format key metrics clearly with labels

Historical Data:
- Show date range, highlight key points (highs, lows, trends)
- Format dates in readable format (e.g., "January 15, 2025" not "2025-01-15")

Earnings Data:
- Extract relevant earnings figures, EPS, revenue
- Show dates and comparisons if available

Error Handling:
- If API returns an error message, explain what went wrong
- If data is missing, say "No data available for [query]"
- If there's a rate limit, suggest trying again later

OUTPUT FORMAT:
Provide a clear, direct answer. Do NOT include:
- Technical jargon unless necessary
- JSON structure explanations
- API endpoint details
- Debugging information

Just answer the user's question in plain English.
"""

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def call_agent(system_prompt: str, model: str = "claude-sonnet-4-20250514") -> str:
    """Call a specialized agent and return its response."""
    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": "Execute your task."}]
    )

    text = ""
    for block in response.content:
        if hasattr(block, "text"):
            text += block.text

    return text


def extract_python_code(text: str) -> list:
    """Extract Python code blocks from text."""
    code_blocks = []
    lines = text.split('\n')
    in_code_block = False
    current_block = []

    for line in lines:
        if line.strip().startswith('```python'):
            in_code_block = True
            current_block = []
        elif line.strip() == '```' and in_code_block:
            in_code_block = False
            if current_block:
                code_blocks.append('\n'.join(current_block))
        elif in_code_block:
            current_block.append(line)

    return code_blocks


def execute_python_code(code: str, working_dir: str) -> dict:
    """Execute Python code and return results."""
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, dir=working_dir) as f:
            f.write(code)
            temp_file = f.name

        result = subprocess.run(
            [sys.executable, temp_file],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=working_dir
        )

        os.unlink(temp_file)

        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
            "success": result.returncode == 0
        }

    except subprocess.TimeoutExpired:
        return {
            "stdout": "",
            "stderr": "Execution timed out after 30 seconds",
            "returncode": -1,
            "success": False
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
            "success": False
        }


# ============================================================================
# 5-AGENT PIPELINE
# ============================================================================

def run_pipeline(user_query: str):
    """Run the 5-agent pipeline: Explorer → Reader → Coder → Executor → Parser"""

    # Initialize client if not already done (when imported as module)
    global client
    if client is None:
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")
        client = anthropic.Anthropic(api_key=api_key)

    print("\n" + "="*70)
    print("5-AGENT PIPELINE: Explorer → Reader → Coder → Executor → Parser")
    print("="*70)

    # ========================================================================
    # STAGE 1A: EXPLORER - DISCOVERY
    # ========================================================================
    print("\n[1a/4] 🔍 EXPLORER AGENT (Discovery) - Finding all available tools...")
    print("-"*70)

    discovery_response = call_agent(EXPLORER_DISCOVERY_PROMPT)

    # Execute discovery code
    code_blocks = extract_python_code(discovery_response)
    available_tools_list = []

    if code_blocks:
        result = execute_python_code(code_blocks[0], WORKING_DIR)
        if result["success"]:
            print(result["stdout"])
            # Parse the tool list from stdout
            for line in result["stdout"].split('\n'):
                if line.strip().startswith('- '):
                    tool_name = line.strip()[2:].strip()
                    available_tools_list.append(tool_name)
        else:
            print("❌ Discovery failed:")
            print(result["stderr"])
            return {"success": False, "answer": "Tool discovery failed", "tool_used": None, "generated_code": None, "raw_api_response": None}
    else:
        print("❌ No discovery code generated")
        return {"success": False, "answer": "No discovery code generated", "tool_used": None, "generated_code": None, "raw_api_response": None}

    if not available_tools_list:
        print("❌ No tools discovered")
        return {"success": False, "answer": "No tools discovered", "tool_used": None, "generated_code": None, "raw_api_response": None}

    # ========================================================================
    # STAGE 1B: EXPLORER - SELECTION
    # ========================================================================
    print(f"\n[1b/4] 🎯 EXPLORER AGENT (Selection) - Choosing best tool for query...")
    print("-"*70)

    # Format the tools list for the selection prompt
    tools_formatted = "\n".join([f"  - {tool}" for tool in available_tools_list])

    selection_prompt = EXPLORER_SELECTION_PROMPT.format(
        user_query=user_query,
        available_tools=tools_formatted
    )
    selection_response = call_agent(selection_prompt)

    # Extract selected tool
    selected_tool = None
    for line in selection_response.split('\n'):
        if line.startswith('SELECTED_TOOL:'):
            selected_tool = line.replace('SELECTED_TOOL:', '').strip()
            break

    if not selected_tool:
        print("❌ Explorer failed to select a tool")
        print("Response:", selection_response)
        return {"success": False, "answer": "Failed to select appropriate tool", "tool_used": None, "generated_code": None, "raw_api_response": None}

    print(f"✓ Selected: {selected_tool}")

    # ========================================================================
    # STAGE 2: READER (Understand Tool)
    # ========================================================================
    print(f"\n[2/4] 📖 READER AGENT - Reading {selected_tool}.py...")
    print("-"*70)

    # Read the tool file directly using absolute path
    tool_file_path = os.path.join(WORKING_DIR, "servers", "alphavantage", f"{selected_tool}.py")

    try:
        with open(tool_file_path, 'r') as f:
            tool_content = f.read()
        print(f"✓ Read {len(tool_content)} characters from {selected_tool}.py")
    except FileNotFoundError:
        print(f"❌ Tool file not found: {tool_file_path}")
        return {"success": False, "answer": f"Tool file not found: {selected_tool}", "tool_used": selected_tool, "generated_code": None, "raw_api_response": None}
    except Exception as e:
        print(f"❌ Error reading tool file: {e}")
        return {"success": False, "answer": f"Error reading tool file: {e}", "tool_used": selected_tool, "generated_code": None, "raw_api_response": None}

    # Now call the reader agent with the actual file content
    reader_prompt = READER_PROMPT.format(
        tool_name=selected_tool,
        tool_content=tool_content
    )
    reader_response = call_agent(reader_prompt)

    # Extract and display interface summary
    print("\nTool Interface:")
    interface_start = reader_response.find("TOOL:")
    if interface_start >= 0:
        # Display the full interface extraction
        interface_end = reader_response.find("EXAMPLE_CALL:")
        if interface_end >= 0:
            interface_end = reader_response.find("\n", interface_end + 100)  # Include example call
            if interface_end < 0:
                interface_end = len(reader_response)
        else:
            interface_end = len(reader_response)
        interface_summary = reader_response[interface_start:interface_end]
        print(interface_summary)

    # ========================================================================
    # STAGE 3: CODER (Generate Code)
    # ========================================================================
    print(f"\n[3/4] 💻 CODER AGENT - Generating executable code...")
    print("-"*70)

    coder_prompt = CODER_PROMPT.format(
        user_query=user_query,
        tool_name=selected_tool,
        tool_interface=reader_response
    )
    coder_response = call_agent(coder_prompt)

    print("\nGenerated Code:")
    code_blocks = extract_python_code(coder_response)
    if code_blocks:
        print(code_blocks[0])

    # ========================================================================
    # STAGE 4: EXECUTE GENERATED CODE
    # ========================================================================
    if code_blocks:
        print("\n[4/5] ⚡ EXECUTING CODE...")
        print("="*70 + "\n")

        result = execute_python_code(code_blocks[0], WORKING_DIR)

        if result["success"]:
            print("Raw API Response:")
            print(result["stdout"])
            api_response = result["stdout"]
        else:
            print("❌ Execution failed:")
            print(result["stderr"])
            api_response = result["stderr"]

        # ====================================================================
        # STAGE 5: PARSER (Format Response)
        # ====================================================================
        print(f"\n[5/5] 📝 PARSER AGENT - Formatting response...")
        print("-"*70 + "\n")

        parser_prompt = PARSER_PROMPT.format(
            user_query=user_query,
            tool_name=selected_tool,
            api_response=api_response
        )
        parser_response = call_agent(parser_prompt)

        print("="*70)
        print("FINAL ANSWER")
        print("="*70)
        print(parser_response)
        print("="*70)

        # Return structured response for API usage
        return {
            "success": True,
            "answer": parser_response,
            "tool_used": selected_tool,
            "generated_code": code_blocks[0] if code_blocks else None,
            "raw_api_response": api_response
        }
    else:
        print("\n❌ No code generated")
        return {
            "success": False,
            "answer": "Failed to generate code",
            "tool_used": selected_tool if 'selected_tool' in locals() else None,
            "generated_code": None,
            "raw_api_response": None
        }


# ============================================================================
# MAIN CLI
# ============================================================================

def main():
    """Main CLI loop."""
    print("="*70)
    print("Multi-Agent Alpha Vantage Assistant (5-Agent Architecture)")
    print("="*70)
    print("\n🏗️  Pipeline Architecture:")
    print("  1a. 🔍 EXPLORER (Discovery) - Scans filesystem for all tools")
    print("  1b. 🎯 EXPLORER (Selection) - Selects best tool from discovered list")
    print("  2.  📖 READER              - Reads tool file + extracts interface")
    print("  3.  💻 CODER               - Generates executable code")
    print("  4.  ⚡ EXECUTOR             - Runs generated code")
    print("  5.  📝 PARSER              - Formats response into natural language")
    print("\n" + "="*70)
    print("\nCommands:")
    print("  Type your query and press Enter")
    print("  'exit' or 'quit' to exit")
    print("="*70)
    print("\nExample queries:")
    print("  - What's the current price of Tesla?")
    print("  - Show me Apple's company overview")
    print("  - Get the last 5 days of NVDA stock data")
    print("="*70)

    while True:
        try:
            user_input = input("\n\n💬 You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 Goodbye!")
                break

            # Run the 5-agent pipeline
            run_pipeline(user_input)

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n\n❌ Error: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
