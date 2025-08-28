from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from duckduckgo_search import DDGS
from tools import search_tool, wiki_tool, save_tool  # Import tools from tools.py

load_dotenv()  # Loading environment variables from .env file

class ResearchAgentOutput(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
    references: list[str]

llm= ChatOpenAI(model_name="gpt-5",)  # Initializing OpenAI LLM
parser=PydanticOutputParser(pydantic_object=ResearchAgentOutput)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user queries and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools=[search_tool,wiki_tool,save_tool]  # Add tools here
agent=create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools,  
)

agent_executor=AgentExecutor(agent=agent,tools=tools, verbose=True)
query=input("What can I help you Research today? ")
raw_response=agent_executor.invoke({"query": query})

try:
    sturctured_response=parser.parse(raw_response.get("output")[0]["text"])
except Exception as e:    
    print("Error parsing response:", e," Raw response:", raw_response)