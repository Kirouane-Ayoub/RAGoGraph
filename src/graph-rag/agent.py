from cypher import chain
from langchain.agents import AgentType, Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI

tools = [
    Tool(
        name="graph-rag",
        func=chain.invoke,
        description="Useful for retrieving information from a graph database, if you did not get any result from this tool , say it didn't mentioned in the database.",
    )
]
memory = ConversationBufferMemory(memory_key="chat_history")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True,
    max_iterations=3,
    early_stopping_method="generate",
)
