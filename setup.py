"""
Environment Initialization & Setup Script.
Prepares system directories, creates initial configuration, and validates runtime dependencies.
"""

import os
from pathlib import Path
from src.logger import get_logger

logger = get_logger("setup")

REQUIRED_DIRS = [
    Path("./data"),
    Path("./vectorstore"),
    Path("./logs")
]

def run_setup():
    logger.info("Initializing RAG Search Assistant environment setup...")

    # 1. Create essential system directories
    for folder in REQUIRED_DIRS:
        folder.mkdir(parents=True, exist_ok=True)
        logger.info(f"Verified directory: [bold green]{folder.resolve()}[/bold green]")

    # 2. Handle environment settings initialization
    env_file = Path(".env")
    env_example = Path(".env.example")

    if not env_file.exists():
        if env_example.exists():
            env_file.write_text(env_example.read_text(encoding="utf-8"), encoding="utf-8")
            logger.warning("Created `.env` from template. [bold yellow]Please edit `.env` and add yoyr OPENAI_API_KEY.[/bold yellow]")
        else:
            logger.error("Failed to find `env.example` template.")
    else:
        logger.info("`.env` file present.")

    logger.info("System setup initialization complete.")

if __name__=="__main__":
    run_setup()