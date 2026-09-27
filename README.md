# Document-Based RAG Search Assistant

An enterprise-grade, local RAG (Retrieval-Augmented Generation) system built in Python. Designed with strict guardrails to eliminate hallucination, preserve document metadata citations, and offer sub-second document retrieval over `.txt`, `.md`, and `.pdf` files.

## 🌟 Key Features
- **Strict Guardrail Fallbacks**: Detects low relevance scores and gracefully refuses unanswerable queries.
- **Local Hugging Face Embeddings**: Employs `sentence-transformers/all-MiniLM-L6-v2` locally for zero API token cost.
- **Source Citation & Confidence Scoring**: Provides document filenames, page numbers, and cosine relevance scores for every output.
- **Interactive CLI UI**: Formatted console terminal with `rich` panels, spinners, and structured citation tables.
- **Clean Modular Architecture**: Separated ingestion, vector storage, RAG reasoning, and runtime configuration using Pydantic Settings.

## 📁 Architecture Overview
```text
doc-rag-assistant/
├── data/              # Source documents (.pdf, .txt, .md)
├── vectorstore/       # Persistent local ChromaDB storage
├── src/
│   ├── config.py      # Pydantic environment validation
│   ├── document_loader.py # Cleaning, parsing, and chunking
│   ├── vector_store.py# ChromaDB + Hugging Face local embeddings
│   ├── rag_engine.py  # LLM generation & guardrail fallbacks
│   └── logger.py      # Dual console and file logger
├── ingest.py          # Document ingestion script
├── main.py            # CLI query application entry point
└── tests/             # Automated Pytest suite
