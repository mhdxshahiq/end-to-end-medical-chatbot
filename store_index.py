from dotenv import load_dotenv
import os
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

# CRITICAL FIX: You must call this to read the .env file!
load_dotenv()

# Get the keys
pinecone_api_key = os.getenv("PINECONE_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY")

# Safety Check: Stop the code if keys are missing
if not pinecone_api_key or not google_api_key:
    raise ValueError("Missing API Keys! Check if PINECONE_API_KEY and GOOGLE_API_KEY are in your .env file.")

# Initialize Pinecone
pc = Pinecone(api_key=pinecone_api_key)

# Initialize Embeddings
# Make sure 'embedding' is defined (calling your helper function)
embedding = download_embeddings()

index_name = "medical-chatbot"

# Connect to Existing Index
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

print("✅ Successfully connected to existing Pinecone index.")