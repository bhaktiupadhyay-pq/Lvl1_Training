from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain.chains.retrieval_qa.base import RetrievalQA

DATA_PATH = "data/sample.pdf"

print("\nLoading PDF...")
loader = PyPDFLoader(DATA_PATH)
documents = loader.load()

print("Splitting documents...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating vector store...")
vectorstore = FAISS.from_documents(chunks, embeddings)

retriever = vectorstore.as_retriever()

print("Loading local LLM with Ollama...")
llm = OllamaLLM(model="llama3")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

print("\n===== SIMPLE LOCAL RAG PIPELINE =====")

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    response = qa_chain.invoke(query)

    print("\nAnswer:")
    print(response)