"""Test para verificar que todo está configurado correctamente"""
import os
from config.settings import Settings
from langchain_openai import ChatOpenAI
from rich.console import Console

console = Console()

def test_environment():
    """Verificar entorno Python"""
    console.print("[bold]Testing Python Environment...[/bold]")
    import sys
    print(f"Python version: {sys.version}")
    
def test_api_keys():
    """Verificar API keys"""
    console.print("[bold]Testing API Keys...[/bold]")
    
    if Settings.OPENAI_API_KEY:
        console.print("✅ OpenAI API Key found")
    else:
        console.print("❌ OpenAI API Key missing")
        
def test_openai_connection():
    """Test conexión con OpenAI"""
    console.print("[bold]Testing OpenAI Connection...[/bold]")
    
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",  # Usar modelo más barato para test
            temperature=0
        )
        
        response = llm.invoke("Say 'Hello World' if you can hear me!")
        console.print(f"✅ OpenAI Response: {response.content}")
        
    except Exception as e:
        console.print(f"❌ OpenAI Error: {str(e)}")

def test_langchain():
    """Test LangChain básico"""
    console.print("[bold]Testing LangChain...[/bold]")
    
    try:
        from langchain.schema import HumanMessage
        from langchain_openai import ChatOpenAI
        
        console.print("✅ LangChain imports successful")
        
    except Exception as e:
        console.print(f"❌ LangChain Error: {str(e)}")

def run_all_tests():
    """Ejecutar todos los tests"""
    console.print("[bold green]🚀 Starting Environment Setup Tests[/bold green]\n")
    
    test_environment()
    test_api_keys()
    test_langchain()
    test_openai_connection()
    
    console.print("\n[bold green]✅ Setup tests completed![/bold green]")

if __name__ == "__main__":
    run_all_tests()