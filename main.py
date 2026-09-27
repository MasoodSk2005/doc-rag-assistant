"""
Main Application Entry Point.
Provides an interactive CLI interface with rich UI rendering fro document RAG querying.
"""
import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from src.rag_engine import RAGEngine
from src.logger import get_logger
from ingest import run_ingestion

logger = get_logger("main")
console = Console()

def display_sources(sources: list):
    """Renders document citation metadata in a styled console table."""
    if not sources:
        return

    table = Table(title="Attributed Sources & Relevance", show_header=True, header_style="bold cyan")
    table.add_column("Document Name", style="bold green")
    table.add_column("Page / Section", justify="center")
    table.add_column("Cosine Distance", justify="right")
    table.add_column("Confidence Proxy", justify="right", style="bold yellow")

    for src in sources:
        table.add_row(
            str(src["source_name"]),
            str(src["page"]),
            f"{src['relevance_distance']:.4f}",
            f"{src['Confidence_score'] * 100:.1f}%"
        )
    console.print(table)

def main():
    console.print(Panel.fit("[bold green]Document-Based RAG Search Assistant[/bold green]\nType [bold red]'exit'[/bold red] to quit, or [bold yellow]'--ingest'[/bold yellow] to process /data files.", title="System Active"))

    engine= RAGEngine()

    while True:
        try:
            query = Prompt.ask("\n[bold cyan]Enter Query[/bold cyan]").strip()

            if not query:
                continue

            if query.lower() in {"exit", "quit", "q"}:
                console.print("[bold yellow]Exiting Assistant. Goodbye![/bold yellow]")
                sys.exit(0)

            if query.lower() == "__ingest":
                run_ingestion()
                continue

            # Execute RAG query pipeline
            with console.status("[bold green]Searching context & generating response...[/bold green]"):
                result = engine.answer_query(query)

            # Render Answer Panel
            border_style = "red" if result["fallback_triggered"] else "green"
            console.print(Panel(result["answer"], title="[bold]Response[/bold]", border_style=border_style))

            # Render Metadata Table
            if result["sources"]:
                display_sources(result["sources"])

        except KeyboardInterrupt:
            console.print("\n[bold yellow]Exiting Assistant. Goodbye![/bold yellow]")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Unexpected runtime error: {str(e)}")

if __name__ == "__main__":
    main()