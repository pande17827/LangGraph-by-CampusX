import os
from langgraph.graph import StateGraph ,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()
# Load API key
api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key  # Set it for LangChain usage

# Initialize Gemini model (text only)
llm_model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


# creating states
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


# initializing the graph
graph=StateGraph(ChatState)


# creating node function and embedding the nodes
def chat_node(state: ChatState):
    messages = state['messages']
    response = llm_model.invoke(messages)

    # Append the response to the messages
    return {'messages': messages + [response]}  # ✅ Append, don't wrap in another list


graph.add_node('chat_node',chat_node)

# adding edges
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)


# creating the checkpointer object
checkpointer=InMemorySaver()


# evaluating the graph with checkpointer
chatbot=graph.compile(checkpointer=checkpointer)


