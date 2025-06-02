from typing import Any, Dict
import json
from rich.console import Console
from rich.table import Table

console = Console()

def print_agent_response(response: Any, title: str = "Agent Response"):
    """Pretty print agent responses"""
    console.print(f"\n[bold blue]{title}[/bold blue]")
    console.print(f"[green]{response}[/green]")

def print_error(error: str):
    """Pretty print errors"""
    console.print(f"[bold red]Error: {error}[/bold red]")

def save_conversation(conversation: list, filename: str):
    """Guardar conversación en JSON"""
    with open(f"conversations/{filename}.json", "w") as f:
        json.dump(conversation, f, indent=2)

def create_summary_table(data: Dict[str, Any]):
    """Crear tabla resumen"""
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Property")
    table.add_column("Value")
    
    for key, value in data.items():
        table.add_row(key, str(value))
    
    return table