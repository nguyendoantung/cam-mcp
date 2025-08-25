# from mcp_use import MCPClient
# from langchain_openai import ChatOpenAI # Example LLM

# config = {
#     "mcpServers": {
#         "my_http_server": {
#             "url": "http://localhost:8000/mcp" # Adjust port and endpoint as needed
#         }
#     }
# }
# client = MCPClient.from_dict(config)
# llm = ChatOpenAI(model="gpt-4o") # Initialize your LLM
# agent = MCPAgent(llm=llm, client=client)

# # Now you can use the agent to interact with your MCP server's tools
# result = await agent.run("Use the 'add' tool to calculate 5 plus 3.")

from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
config = {"mcpServers": {"my_http_server": {"url": "http://localhost:8000/mcp"}}}

# Initialize the client with the MCP server URL
client = genai.Client(location=config["mcpServers"]["my_http_server"]["url"])

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="what weather is it in Vietnam?"
)
