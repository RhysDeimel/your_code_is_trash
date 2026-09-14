from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient

# GitHub MCP server runs via Docker; uses the built-in OAuth app (browser login on
# first use, token kept in memory only) instead of a PAT. Requires a loopback
# callback port published so the container's login redirect is reachable.
github_mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="docker",
        args=[
            "run", "-i", "--rm",
            "-p", "127.0.0.1:8085:8085",
            "-e", "GITHUB_OAUTH_CALLBACK_PORT",
            "-e", "GITHUB_TOOLSETS=pull_requests",
            "ghcr.io/github/github-mcp-server"
        ],
        env={"GITHUB_OAUTH_CALLBACK_PORT": "8085"}
    )
))

# Pass MCP clients directly to agent - lifecycle managed automatically
agent = Agent(tools=[github_mcp_client])
agent("What is the most recent pull request open in the foo repo?")