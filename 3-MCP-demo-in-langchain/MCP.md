# MCP Concept 

## MCP Flow

![mcp-server](./flowcharts/1-mcp-server.svg)

Above diagram represent the overall conceptual designing goes behing the MCP architecture.

## MCP with Agent/LLM

![mcp-with-agent](./flowcharts/2-mcp-with-agent.svg)

## Finally Achived MCP Communication:

- Created MCP Client & communicated 2 MCP Servers

    - To `math server` with `stdio` protocol. (communicating with `terminal / command prompt`)
    - To `weather server` with `http` protocol. (communicating with `url`)

![mcp-protocol](./flowcharts/3-mcp-protocol.svg)