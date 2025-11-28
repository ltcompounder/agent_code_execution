#!/usr/bin/env python3
"""
Simple test script for the FastAPI server
"""

import requests
import json
import sys

BASE_URL = "http://localhost:8000"


def test_health():
    """Test the health endpoint"""
    print("Testing /health endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    return response.status_code == 200


def test_root():
    """Test the root endpoint"""
    print("Testing / endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    return response.status_code == 200


def test_query(query: str, include_debug: bool = False):
    """Test the query endpoint"""
    print(f"Testing /query endpoint with: '{query}'")
    print(f"Debug mode: {include_debug}\n")

    payload = {
        "query": query,
        "include_debug": include_debug
    }

    response = requests.post(
        f"{BASE_URL}/query",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    print(f"Status: {response.status_code}")

    if response.status_code == 200:
        result = response.json()
        print(f"Success: {result.get('success')}")
        print(f"Tool Used: {result.get('tool_used')}")
        print(f"\nAnswer:\n{result.get('answer')}\n")

        if include_debug and result.get('debug_info'):
            print("Debug Info Available:")
            debug = result.get('debug_info', {})
            print(f"  - Selected Tool: {debug.get('selected_tool')}")
            if debug.get('generated_code'):
                print(f"  - Generated Code: Available ({len(debug.get('generated_code', ''))} chars)")
            if debug.get('raw_api_response'):
                print(f"  - Raw API Response: Available ({len(debug.get('raw_api_response', ''))} chars)")
            print()

        return result.get('success', False)
    else:
        print(f"Error: {response.text}\n")
        return False


def main():
    """Run all tests"""
    print("="*70)
    print("FastAPI Server Test Suite")
    print("="*70)
    print(f"Testing server at: {BASE_URL}\n")

    try:
        # Test health endpoint
        if not test_health():
            print("❌ Health check failed")
            sys.exit(1)

        # Test root endpoint
        if not test_root():
            print("❌ Root endpoint failed")
            sys.exit(1)

        # Test query endpoint - simple query
        print("="*70)
        if not test_query("What's the current price of Tesla?"):
            print("❌ Simple query failed")
            sys.exit(1)

        # Test query endpoint - with debug
        print("="*70)
        if not test_query("What's the current price of Apple?", include_debug=True):
            print("❌ Query with debug failed")
            sys.exit(1)

        print("="*70)
        print("✓ All tests passed!")
        print("="*70)

    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to API server")
        print(f"Make sure the server is running at {BASE_URL}")
        print("\nStart the server with: python api.py")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
