import typer
from dotenv import set_key, dotenv_values, load_dotenv
from pathlib import Path
import os
from upllm.providers.vastai import VastAIProvider

# Explicitly load .env file
load_dotenv(dotenv_path=Path(".env"))


app = typer.Typer(help="UPLLM: Spin up cloud instances running Ollama models.")

ENV_FILE = Path(".env")


@app.command()
def set_api_key(provider: str, api_key: str):
    """
    Set API key for a provider.

    Args:
        provider (str): The name of the provider.
        api_key (str): The API key to set.
    """
    set_key(str(ENV_FILE), f"{provider.upper()}_API_KEY", api_key)
    typer.echo(f"🔑 API key set for {provider}.")


@app.command()
def show_api_key(provider: str):
    """
    Show current API key for a provider.

    Args:
        provider (str): The name of the provider.
    """
    keys = dotenv_values(ENV_FILE)
    key = keys.get(f"{provider.upper()}_API_KEY")
    if key:
        typer.echo(f"🔑 Current API key for {provider}: {key}")
    else:
        typer.echo(f"⚠️ No API key set for {provider}.")


@app.command()
def create(
    model: str = typer.Argument(...,
                                help="Name of the Ollama model to deploy"),
    provider: str = typer.Option("vastai", help="Cloud provider to use"),
    gpu: str = typer.Option("RTX 3090", help="GPU type for Vast.ai"),
):
    if provider == "vastai":
        api_key = os.getenv("VASTAI_API_KEY")
        if not api_key:
            typer.echo(
                "⚠️ API key for Vast.ai not set. Use `upllm set-api-key vastai <KEY>`")
            raise typer.Exit(code=1)
        vastai = VastAIProvider(api_key=api_key)
        instance_id = vastai.create_instance(model=model, gpu_type=gpu)
        typer.echo(f"✅ Vast.ai instance created: {instance_id}")
    else:
        typer.echo(f"⚠️ Provider '{provider}' not yet supported.")


if __name__ == "__main__":
    app()
