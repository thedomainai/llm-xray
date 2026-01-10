"""
Main entry point for LLM X-Ray.
"""

import asyncio
import click
from rich.console import Console

console = Console()

@click.group()
def main():
    """LLM X-Ray: Debug the thought process."""
    pass

@main.command()
@click.option("--port", default=8080, help="Port to run the proxy on.")
@click.option("--ui/--no-ui", default=True, help="Launch the TUI dashboard.")
def start(port: int, ui: bool):
    """Start the X-Ray proxy and dashboard."""
    console.print(f"[bold green]Starting LLM X-Ray on port {port}...[/bold green]")
    
    if ui:
        # Import UI here to avoid heavy dependencies on simple --help
        from .ui.app import XRayApp
        app = XRayApp()
        app.run()
    else:
        # Headless mode (just proxy)
        # TODO: Implement headless runner
        console.print("Headless mode started. (Proxy implementation pending)")

if __name__ == "__main__":
    main()
