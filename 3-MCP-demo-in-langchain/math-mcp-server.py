from mcp.server.fastmcp import FastMCP
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

mcp = FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """
    Add two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: final result
    """
    return a+b

@mcp.tool()
def multiply(a:int, b:int) -> float:
    """
    Multiply two numbers

    Args:
        a (int): first number
        b (int): second number

    Returns:
        float: final result
    """
    return a*b

# The transport="stdio" arguments tells the server to:

# Use standard input/output (stdin and stdout) to receive and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")