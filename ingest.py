"""
Document Ingestion Pipeline.
Loads files from /data, chunks them with metadata, and persists vectors to ChromaDB.
"""

from src.document_loader import DocumentProcessor
from src.vector_store import VectorStoreManager
from src.logger import get_logger

logger = get_logger("ingest")


def run_ingestion():
    logger.info("Starting document ingestion pipeline...")

    # 1. Process and chunk raw files
    processor = DocumentProcessor()
    chunks = processor.process_and_chunk()

    if not chunks:
        logger.error("No valid document chunks generated. Ensure files exist in `./data`.")
        return

    # 2. Add chunks into vector store cleanly
    manager = VectorStoreManager()
    success = manager.index_documents(chunks, clean_existing=True)

    if success:
        logger.info(f"Ingestion successful! Persisted {len(chunks)} chunk(s) into vector store.")
    else:
        logger.error("Failed to index documents into vector store.")


if __name__ == "__main__":
    run_ingestion()