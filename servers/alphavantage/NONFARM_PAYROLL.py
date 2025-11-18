
from servers.mcp_client import call_mcp_tool


def NONFARM_PAYROLL(params: dict = None) -> dict:
    """
    
This API returns the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), 
a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, 
unpaid volunteers, farm employees, and the unincorporated self-employed.

Args:
    datatype: By default, datatype=csv. Strings json and csv are accepted with the following specifications: 
              json returns the time series in JSON format; csv returns the time series as a CSV (comma separated value) file.

Returns:
    Nonfarm payroll time series data in JSON format or CSV string.

    
    Args:
        params: Dictionary containing the tool parameters (default: empty dict)
        
    Returns:
        Response from Alpha Vantage MCP server
    """
    if params is None:
        params = {}
    return call_mcp_tool("NONFARM_PAYROLL", params)


# Example usage (if run directly):
if __name__ == "__main__":
    import json
    
    # Example call - modify parameters as needed
    print("Testing NONFARM_PAYROLL...")
    result = NONFARM_PAYROLL()
    print(json.dumps(result, indent=2))
