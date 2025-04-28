# core/tool_registry.py

from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_tool_calling_agent, AgentExecutor
from core.ai_connector import model

# Import your custom functions
from functions.get_products import get_products

@tool
def get_products_tool(query: str):
    """Fetch products dynamically based on user query like winter jackets, wedding sherwanis, etc."""
    return get_products(query)

def get_registered_tools():
    return [get_products_tool]

def build_agent():
    tools = get_registered_tools()

    # System behavior prompt
    system_prompt = ChatPromptTemplate.from_messages([
        ("system", "You are ABHYUM's intelligent shopping assistant. Help users with smart, polite, helpful product suggestions and information."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ])

    # Create a Gemini-compatible tool-calling agent
    agent = create_tool_calling_agent(
        llm=model,
        prompt=system_prompt,
        tools=tools
    )

    executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return executor