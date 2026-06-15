# AI Research Mind

An AI-powered Research Assistant built using FastAPI, Streamlit, Ollama (Llama 3), and ChromaDB. The application enables users to upload research papers, academic notes, and PDF documents, perform semantic search across multiple documents, and interact with their knowledge base through a conversational AI interface powered by Retrieval-Augmented Generation (RAG).

## Features

* PDF Upload and Processing
* Automated Text Extraction
* Intelligent Text Chunking
* Vector Embedding Generation
* ChromaDB Vector Storage
* Semantic Search and Retrieval
* Retrieval-Augmented Generation (RAG)
* Multi-Document Knowledge Search
* Conversational Memory
* Local LLM Inference using Ollama and Llama 3
* ChatGPT-Style User Interface
* Interactive Streamlit Frontend
* FastAPI Backend Architecture
* Modular and Scalable Code Structure

## System Architecture

User Uploads PDF
↓
FastAPI Backend
↓
PDF Parser
↓
Text Chunking
↓
Embeddings Generation
↓
ChromaDB Vector Store
↓
Semantic Retrieval
↓
Ollama (Llama 3)
↓
AI Generated Response
↓
Streamlit Chat Interface

## Tech Stack

### Backend

* FastAPI
* Python
* Uvicorn

### AI & RAG

* Ollama
* Llama 3
* ChromaDB
* LangChain

### Frontend

* Streamlit

### Document Processing

* PyMuPDF (fitz)

## Project Structure

AI-Research-Mind/

├── app/

│ ├── routes/

│ ├── services/

│ ├── main.py

│

├── frontend/

│ └── app.py

│

├── uploads/

├── chroma_db/

├── requirements.txt

├── .gitignore

└── README.md

## Installation

### Clone Repository

git clone <repository-url>

cd AI-Research-Mind

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows:

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Start Ollama

ollama run llama3

### Start Backend

uvicorn app.main:app --reload

### Start Frontend

streamlit run frontend/app.py

Usage

1. Launch the Streamlit application.
2. Upload one or more PDF documents.
3. Wait for document processing and indexing.
4. Ask questions related to uploaded documents.
5. Receive context-aware responses generated using Retrieval-Augmented Generation.
6. Explore retrieved context supporting each answer.

 Current Capabilities

* Semantic document search
* Multi-document retrieval
* Local AI inference
* Context-aware question answering
* Conversational interaction with uploaded PDFs
* Persistent vector storage using ChromaDB

Future Enhancements

* Source Citations and Page References
* Research Paper Generation
* LangGraph Multi-Agent Workflow
* Literature Review Automation
* Citation Generation
* Knowledge Graph Construction
* Academic Paper Templates
* Export to PDF and DOCX
* Research Workspace Management
* User Authentication

## Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Vector Databases
* Semantic Search
* FastAPI Development
* Streamlit Application Development
* AI System Design
* Document Intelligence Systems
* Conversational AI
* End-to-End Full Stack AI Engineering

 Author

Sanidhya Borade

Computer Engineering Student

AI | Machine Learning | Full Stack Development | Generative AI

Building intelligent systems that transform information into actionable knowledge.
