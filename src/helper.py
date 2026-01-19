from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain_core.documents import Document 


#extract text from pdf files
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf", #all pdf files
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents


#extract only source metadata and filter short documents
def filter_to_minimal_docs(docs: List[Document], min_length: int = 1000) -> List[Document]:
    """Contains only 'source' in metadata and filters out short content."""
    minimal_docs: List[Document] = [] 
    
    for doc in docs:
        if len(doc.page_content) >= min_length:
            src = doc.metadata.get("source", "Unknown")
            minimal_docs.append(
                Document(
                    page_content=doc.page_content,
                    metadata={"source": src}
                )
            )
    return minimal_docs


#split text into smaller chucks
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    text_chunks = text_splitter.split_documents(minimal_docs)
    return text_chunks


#downloid embedding model from huggingface
def download_embeddings():
    """Download the embeddings model."""
    # Using a popular, high-quality open-source model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)
    return embeddings
