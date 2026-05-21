
# Simple Beginner-Friendly RAG Pipeline

This project demonstrates a simple Local RAG (Retrieval-Augmented Generation) pipeline using:

- LangChain
- FAISS Vector Database
- HuggingFace Embeddings
- Ollama Local LLM
- PDF Document Retrieval

---

## Features

- Load PDF documents
- Split text into chunks
- Create embeddings
- Store vectors in FAISS
- Retrieve relevant context
- Generate answers using a local LLM

---

## Project Structure

```bash
simple_rag_pipeline_project/
│
├── app.py
├── requirements.txt
├── README.md
└── data/
    └── sample.pdf
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd simple_rag_pipeline_project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install:

https://ollama.com/

Pull llama3 model:

```bash
ollama pull llama3
```

### 5. Add Your PDF

Put your PDF file inside:

```bash
data/sample.pdf
```

### 6. Run Project

```bash
python app.py
```

---

## Example Questions

```bash
What is this document about?
Summarize the PDF.
Explain key topics from the document.
```

---

## Technologies Used

- Python
- LangChain
- FAISS
- Ollama
- HuggingFace Embeddings

---

## Future Improvements

- Streamlit UI
- Chat history
- Multi-PDF support
- ChromaDB integration
- Web interface
