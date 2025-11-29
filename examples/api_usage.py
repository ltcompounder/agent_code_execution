#!/usr/bin/env python3
"""
Examples of using the Multi-Agent Alpha Vantage API

This script demonstrates various ways to interact with the API
"""

import requests
import json


# Base URL for the API
BASE_URL = "http://localhost:8000"


def query_stock_price(symbol: str):
    """Example: Get current stock price"""
    print(f"\n{'='*70}")
    print(f"Example 1: Current Stock Price for {symbol}")
    print('='*70)

    response = requests.post(
        f"{BASE_URL}/query",
        json={"query": f"What's the current price of {symbol}?"}
    )

    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print(f"\nTool Used: {result['tool_used']}")
            print(f"\nAnswer:\n{result['answer']}")
        else:
            print(f"Error: {result.get('error')}")
    else:
        print(f"HTTP Error: {response.status_code}")


def query_company_overview(symbol: str):
    """Example: Get company overview"""
    print(f"\n{'='*70}")
    print(f"Example 2: Company Overview for {symbol}")
    print('='*70)

    response = requests.post(
        f"{BASE_URL}/query",
        json={"query": f"Tell me about {symbol} company"}
    )

    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print(f"\nTool Used: {result['tool_used']}")
            print(f"\nAnswer:\n{result['answer']}")


def query_with_debug(query: str):
    """Example: Query with debug information"""
    print(f"\n{'='*70}")
    print(f"Example 3: Query with Debug Information")
    print('='*70)
    print(f"Query: {query}")

    response = requests.post(
        f"{BASE_URL}/query",
        json={
            "query": query,
            "include_debug": True
        }
    )

    if response.status_code == 200:
        result = response.json()
        if result['success']:
            print(f"\nTool Used: {result['tool_used']}")
            print(f"\nAnswer:\n{result['answer']}")

            if result.get('debug_info'):
                print(f"\n--- Debug Information ---")
                debug = result['debug_info']

                # Show selected tool
                print(f"\nSelected Tool: {debug.get('selected_tool')}")

                # Show generated code snippet
                if debug.get('generated_code'):
                    print(f"\nGenerated Code Snippet:")
                    print(debug['generated_code'][:500] + "...")

                # Pipeline output available
                if debug.get('pipeline_output'):
                    print(f"\nFull Pipeline Output Available: {len(debug['pipeline_output'])} characters")


def check_api_health():
    """Example: Check API health"""
    print(f"\n{'='*70}")
    print(f"Example 4: Health Check")
    print('='*70)

    response = requests.get(f"{BASE_URL}/health")

    if response.status_code == 200:
        health = response.json()
        print(f"\nStatus: {health['status']}")
        print(f"Anthropic API Key Set: {'✓' if health['anthropic_api_key_set'] else '✗'}")
        print(f"Alpha Vantage API Key Set: {'✓' if health['alpha_vantage_api_key_set'] else '✗'}")


def batch_queries(queries: list):
    """Example: Run multiple queries"""
    print(f"\n{'='*70}")
    print(f"Example 5: Batch Queries")
    print('='*70)

    results = []

    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] Processing: {query}")

        response = requests.post(
            f"{BASE_URL}/query",
            json={"query": query}
        )

        if response.status_code == 200:
            result = response.json()
            if result['success']:
                results.append({
                    'query': query,
                    'tool': result['tool_used'],
                    'answer': result['answer']
                })
                print(f"✓ Completed using {result['tool_used']}")
            else:
                print(f"✗ Failed: {result.get('error')}")
        else:
            print(f"✗ HTTP Error: {response.status_code}")

    # Show summary
    print(f"\n{'='*70}")
    print("Batch Results Summary")
    print('='*70)
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['query']}")
        print(f"   Tool: {result['tool']}")
        print(f"   Answer: {result['answer'][:100]}...")


def main():
    """Run all examples"""
    print("="*70)
    print("Multi-Agent Alpha Vantage API - Usage Examples")
    print("="*70)
    print(f"\nAPI Server: {BASE_URL}")
    print("\nMake sure the API server is running:")
    print("  python api.py")
    print("\n" + "="*70)

    try:
        # Example 1: Stock price
        query_stock_price("NVDA")

        # Example 2: Company overview
        query_company_overview("AAPL")

        # Example 3: Query with debug info
        query_with_debug("What are the top gainers today?")

        # Example 4: Health check
        check_api_health()

        # Example 5: Batch queries
        batch_queries([
            "What's the current price of Microsoft?",
            "What's the current price of Google?",
            "What's the current price of Amazon?"
        ])

        print(f"\n{'='*70}")
        print("✓ All examples completed!")
        print('='*70)

    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API server")
        print(f"Make sure the server is running at {BASE_URL}")
        print("\nStart the server with: python api.py")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
