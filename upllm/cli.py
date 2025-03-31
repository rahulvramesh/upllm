# upllm/cli.py
import typer
from rich.console import Console

# CLI App
app = typer.Typer(help="Deploy LLMs on cloud providers like Vast.ai and RunPod")
console = Console()

if __name__ == "__main__":
    app()
