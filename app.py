import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from src.helper import download_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import template

app = Flask(__name__, template_folder='src/templates')

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


# 1. Setup Pinecone Connection
embeddings = download_embeddings()
index_name = "medical-chatbot"

# Connect to the index you already created
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Initialize Retriever and Model
retriever = docsearch.as_retriever(search_kwargs={'k': 1})
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)
prompt = ChatPromptTemplate.from_template(template)

# Chat Message History to keep track of conversation
history = ChatMessageHistory()

# 2. Update the chain to map all THREE variables
rag_chain = (
    {
        "context": retriever, 
        "input": RunnablePassthrough(),
        # This maps the 'chat_history' variable expected by the prompt
        "chat_history": lambda x: history.messages[-6:] 
    }
    | prompt
    | model
    | StrOutputParser()
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    print(f"User Question: {msg}") # Look at terminal for this!
    
    try:
        # If the index is empty or name is wrong, this is where it fails
        response = rag_chain.invoke(msg)
        
        # Save to memory
        history.add_user_message(msg)
        history.add_ai_message(response)
        return str(response)
    except Exception as e:
        print(f"CRITICAL ERROR: {str(e)}") # This tells us EXACTLY why it failed
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)