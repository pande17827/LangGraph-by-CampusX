from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Load .env variables
load_dotenv()

# Load API key
api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key  # Set it for LangChain usage

# Initialize Gemini model (text only)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro")


result=llm.invoke("capital of india")
print(result)
print("-"*50)
print(result.content)