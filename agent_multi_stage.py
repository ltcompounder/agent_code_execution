#!/usr/bin/env python3
"""
3-Agent MCP Code Execution Pipeline
Explorer → Reader → Coder
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
if not ANTHROPIC_API_KEY:
    print("Error: ANTHROPIC_API_KEY not set in .env file")
    sys.exit(1)

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

# Working directory
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================================
# AGENT 1: EXPLORER (Discovery + Selection)
# ============================================================================

EXPLORER_PROMPT = """You are a tool explorer agent.

Your task: Scan ./servers/alphavantage/ to find all available tools, then select the best one for the user's query.

User query: {user_query}

Step 1 - Discover all tools (write and execute this code):
```python
import os

try:
    tools_dir = './servers/alphavantage'

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

Step 2 - After seeing all tools, select the most appropriate one for: "{user_query}"

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

Output format:
SELECTED_TOOL: [exact tool name]
"""

# ============================================================================
# AGENT 2: READER (Understanding)
# ============================================================================

READER_PROMPT = """You are a tool reader agent.

Your task: Read the tool file and extract its complete interface.

Tool to read: {tool_name}

Write and execute code to read ./servers/alphavantage/{tool_name}.py

For example, if the tool is GLOBAL_QUOTE, write:
```python
with open('./servers/alphavantage/GLOBAL_QUOTE.py', 'r') as f:
    content = f.read()
    print(content)
```

Now write the code for {tool_name} (use the EXACT tool name in the file path):
```python
# Your code here - replace with actual tool name
```

After reading, carefully analyze the docstring and extract parameters:

IMPORTANT: Look for the "Args:" section in the docstring. Parameters are listed like:
    symbol: Description here
    quarter: Description here
    datatype: Description here (optional)

All parameters in the Args section should be considered REQUIRED unless explicitly marked as "(optional)" or "optional".

Extract and output:

TOOL: {tool_name}
DESCRIPTION: [one-line summary - first line of docstring]
PARAMETERS: [list ALL parameters from Args section with descriptions]
Example format:
  - symbol (REQUIRED): Ticker symbol
  - quarter (REQUIRED): Fiscal quarter in YYYYQM format
  - datatype (OPTIONAL): Data format (json/csv)

EXAMPLE_CALL: {tool_name}({{"param1": "value1", "param2": "value2"}})

Be thorough - list ALL parameters you find in the Args section.
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
4. Prints results in a clear, user-friendly format

Guidelines:
- Wrap code in ```python blocks
- Use try/except for error handling
- Extract relevant fields from API response
- Format output clearly for the user
- Include comments showing parameter format

Example structure:
```python
from servers.alphavantage import {tool_name}

try:
    # Call the tool with parameters in correct format
    result = {tool_name}({{"param": "value"}})  # Use format from documentation!

    # Extract and display relevant data
    if result:
        print("Results:")
        print(result)
    else:
        print("No data returned")

except Exception as e:
    print(f"Error: {{e}}")
```

Generate ONLY the code block, minimal explanation.
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
# 3-AGENT PIPELINE
# ============================================================================

def run_pipeline(user_query: str):
    """Run the 3-agent pipeline: Explorer → Reader → Coder"""

    print("\n" + "="*70)
    print("3-AGENT PIPELINE: Explorer → Reader → Coder")
    print("="*70)

    # ========================================================================
    # STAGE 1: EXPLORER (Discover + Select)
    # ========================================================================
    print("\n[1/3] 🔍 EXPLORER AGENT - Discovering and selecting tool...")
    print("-"*70)

    explorer_prompt = EXPLORER_PROMPT.format(user_query=user_query)
    explorer_response = call_agent(explorer_prompt)

    # Execute discovery code
    code_blocks = extract_python_code(explorer_response)
    if code_blocks:
        result = execute_python_code(code_blocks[0], WORKING_DIR)
        if result["success"]:
            print(result["stdout"])

    # Extract selected tool
    selected_tool = None
    for line in explorer_response.split('\n'):
        if line.startswith('SELECTED_TOOL:'):
            selected_tool = line.replace('SELECTED_TOOL:', '').strip()
            break

    if not selected_tool:
        print("❌ Explorer failed to select a tool")
        print("Response:", explorer_response)
        return

    print(f"\n✓ Selected: {selected_tool}")

    # ========================================================================
    # STAGE 2: READER (Understand Tool)
    # ========================================================================
    print(f"\n[2/3] 📖 READER AGENT - Reading {selected_tool}.py...")
    print("-"*70)

    reader_prompt = READER_PROMPT.format(tool_name=selected_tool)
    reader_response = call_agent(reader_prompt)

    # Execute file reading code
    code_blocks = extract_python_code(reader_response)
    if code_blocks:
        result = execute_python_code(code_blocks[0], WORKING_DIR)
        if result["success"]:
            print(f"✓ Read {len(result['stdout'])} characters")

    # Extract interface summary
    print("\nTool Interface:")
    interface_start = reader_response.find("TOOL:")
    if interface_start >= 0:
        interface_summary = reader_response[interface_start:interface_start+500]
        print(interface_summary.split('\n\n')[0])  # First paragraph only

    # ========================================================================
    # STAGE 3: CODER (Generate Code)
    # ========================================================================
    print(f"\n[3/3] 💻 CODER AGENT - Generating executable code...")
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
    # EXECUTE GENERATED CODE
    # ========================================================================
    if code_blocks:
        print("\n" + "="*70)
        print("⚡ EXECUTING CODE...")
        print("="*70 + "\n")

        result = execute_python_code(code_blocks[0], WORKING_DIR)

        if result["success"]:
            print(result["stdout"])
        else:
            print("❌ Execution failed:")
            print(result["stderr"])
    else:
        print("\n❌ No code generated")


# ============================================================================
# MAIN CLI
# ============================================================================

def main():
    """Main CLI loop."""
    print("="*70)
    print("Multi-Agent Alpha Vantage Assistant (3-Agent Architecture)")
    print("="*70)
    print("\n🏗️  Pipeline Architecture:")
    print("  1. 🔍 EXPLORER - Scans filesystem + selects best tool")
    print("  2. 📖 READER   - Reads tool file + extracts interface")
    print("  3. 💻 CODER    - Generates executable code")
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

            # Run the 3-agent pipeline
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
