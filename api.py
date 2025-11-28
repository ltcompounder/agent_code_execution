#!/usr/bin/env python3
"""
FastAPI server for the Multi-Agent Alpha Vantage Assistant
Exposes the 5-agent pipeline as a REST API
"""

import os
import sys
from typing import Optional
from contextlib import asynccontextmanager
from io import StringIO

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Import the agent pipeline
from agent_multi_stage import run_pipeline

# Verify API keys are set
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not ANTHROPIC_API_KEY:
    print("Warning: ANTHROPIC_API_KEY not set")
if not ALPHA_VANTAGE_API_KEY:
    print("Warning: ALPHA_VANTAGE_API_KEY not set")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown events"""
    # Startup
    print("="*70)
    print("Multi-Agent Alpha Vantage API Server")
    print("="*70)
    print(f"ANTHROPIC_API_KEY: {'✓ Set' if ANTHROPIC_API_KEY else '✗ Not Set'}")
    print(f"ALPHA_VANTAGE_API_KEY: {'✓ Set' if ALPHA_VANTAGE_API_KEY else '✗ Not Set'}")
    print("="*70)
    yield
    # Shutdown
    print("\nShutting down API server...")


# Initialize FastAPI app
app = FastAPI(
    title="Multi-Agent Alpha Vantage API",
    description="5-Agent pipeline for financial data analysis using Alpha Vantage MCP tools",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response models
class QueryRequest(BaseModel):
    """Request model for query endpoint"""
    query: str = Field(
        ...,
        description="Natural language query about financial data",
        example="What's the current price of Tesla?"
    )
    include_debug: bool = Field(
        default=False,
        description="Include debug information (tool selection, generated code, etc.)"
    )


class QueryResponse(BaseModel):
    """Response model for query endpoint"""
    success: bool = Field(description="Whether the query was processed successfully")
    answer: str = Field(description="Natural language answer to the query")
    tool_used: Optional[str] = Field(None, description="Name of the Alpha Vantage tool used")
    debug_info: Optional[dict] = Field(None, description="Debug information if requested")
    error: Optional[str] = Field(None, description="Error message if query failed")


class HealthResponse(BaseModel):
    """Response model for health check"""
    status: str
    anthropic_api_key_set: bool
    alpha_vantage_api_key_set: bool


@app.get("/", tags=["Info"])
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Multi-Agent Alpha Vantage API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "POST /query": "Submit a financial data query",
            "GET /health": "Health check"
        },
        "architecture": "5-Agent Pipeline: Explorer → Reader → Coder → Executor → Parser"
    }


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy" if (ANTHROPIC_API_KEY and ALPHA_VANTAGE_API_KEY) else "degraded",
        anthropic_api_key_set=bool(ANTHROPIC_API_KEY),
        alpha_vantage_api_key_set=bool(ALPHA_VANTAGE_API_KEY)
    )


@app.post("/query", response_model=QueryResponse, tags=["Query"])
async def process_query(request: QueryRequest):
    """
    Process a natural language query using the 5-agent pipeline.

    The pipeline consists of:
    1. Explorer (Discovery) - Finds all available tools
    2. Explorer (Selection) - Selects best tool for query
    3. Reader - Reads tool file and extracts interface
    4. Coder - Generates executable code
    5. Executor - Runs code and gets API response
    6. Parser - Formats response into natural language

    Example queries:
    - "What's the current price of Tesla?"
    - "Show me Apple's company overview"
    - "Get earnings data for NVDA"
    """
    if not ANTHROPIC_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="ANTHROPIC_API_KEY not configured"
        )

    if not ALPHA_VANTAGE_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="ALPHA_VANTAGE_API_KEY not configured"
        )

    try:
        # Capture stdout for debug output (optional)
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        try:
            # Run the 5-agent pipeline and get structured response
            result = run_pipeline(request.query)

            # Get the full output for debug purposes
            full_output = captured_output.getvalue()

        finally:
            # Restore stdout
            sys.stdout = old_stdout

        # Check if pipeline was successful
        if not result or not result.get("success"):
            error_msg = result.get("answer", "Pipeline failed") if result else "Pipeline failed"
            return QueryResponse(
                success=False,
                answer="",
                error=error_msg
            )

        # Prepare debug info if requested
        debug_info = None
        if request.include_debug:
            debug_info = {
                "selected_tool": result.get("tool_used"),
                "generated_code": result.get("generated_code"),
                "raw_api_response": result.get("raw_api_response"),
                "pipeline_output": full_output
            }

        return QueryResponse(
            success=True,
            answer=result.get("answer", ""),
            tool_used=result.get("tool_used"),
            debug_info=debug_info
        )

    except Exception as e:
        import traceback
        error_details = traceback.format_exc()

        return QueryResponse(
            success=False,
            answer="",
            error=f"{str(e)}\n\n{error_details if request.include_debug else ''}"
        )


if __name__ == "__main__":
    import uvicorn

    print("\n" + "="*70)
    print("Starting FastAPI server...")
    print("="*70)
    print("\nAPI will be available at:")
    print("  - http://localhost:8000")
    print("  - Documentation: http://localhost:8000/docs")
    print("  - OpenAPI spec: http://localhost:8000/openapi.json")
    print("\n" + "="*70)

    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
