# 🚀 Paso 1: Entorno Base de Python

Crear entorno virtual
bash# Crear directorio del proyecto
mkdir ai-agents-mastery
cd ai-agents-mastery

## Crear entorno virtual

python -m venv ai-agents-env

## Activar entorno (Windows)

ai-agents-env\Scripts\activate

## Activar entorno (Mac/Linux)

source ai-agents-env/bin/activate
Verificar Python
bashpython --version # Debe ser 3.8+
pip --version

# 📦 Paso 2: Instalación de Dependencias Core

Crear requirements.txt
text# LLM Frameworks
langchain==0.1.20
langchain-openai==0.1.8
langchain-community==0.0.38
langchain-experimental==0.0.60

## Vector Stores & Embeddings

chromadb==0.4.24
faiss-cpu==1.7.4

## Data Processing

pandas==2.0.3
numpy==1.24.3
openpyxl==3.1.2

## Web & APIs

requests==2.31.0
beautifulsoup4==4.12.2
fastapi==0.103.1
uvicorn==0.23.2

## Visualization

matplotlib==3.7.2
plotly==5.15.0
streamlit==1.25.0

## Utilities

python-dotenv==1.0.0
pydantic==2.3.0
rich==13.5.2

## Development

jupyter==1.0.0
pytest==7.4.0
black==23.7.0
Instalar dependencias
bashpip install -r requirements.txt
🔑 Paso 3: Configuración de APIs
Crear archivo .env
bash# En la raíz del proyecto
touch .env # Mac/Linux

## O crear manualmente en Windows

Contenido del .env
env# OpenAI API
OPENAI_API_KEY=tu_api_key_aqui

## Anthropic (opcional)

ANTHROPIC_API_KEY=tu_api_key_aqui

## Google (para búsquedas)

GOOGLE_API_KEY=tu_api_key_aqui
GOOGLE_CSE_ID=tu_cse_id_aqui

## Other APIs (agregaremos más adelante)

SERPAPI_API_KEY=
HUGGINGFACE_API_TOKEN=
Obtener API Keys
OpenAI (OBLIGATORIO)

Ve a platform.openai.com
Crear cuenta si no tienes
Ve a API Keys
Create new secret key
Copia y pega en .env

Google Custom Search (RECOMENDADO)

Ve a console.developers.google.com
Crear proyecto nuevo
Habilitar Custom Search API
Crear credenciales (API Key)
Configurar Custom Search Engine en cse.google.com

# 🏗️ Paso 4: Estructura del Proyecto

Crear estructura de carpetas
bashmkdir -p {agents,tools,memory,config,tests,projects}
mkdir -p projects/{week1,week2,week3}

## Estructura final

ai-agents-mastery/
├── agents/ # Agentes principales
├── tools/ # Herramientas custom
├── memory/ # Sistemas de memoria
├── config/ # Configuraciones
├── tests/ # Tests unitarios
├── projects/ # Proyectos semanales
│ ├── week1/
│ ├── week2/
│ └── week3/
├── notebooks/ # Jupyter notebooks
├── requirements.txt
├── .env
└── README.md

# ⚙️ Paso 5: Configuración Base

Crear config/settings.py
pythonimport os
from dotenv import load_dotenv

load_dotenv()

class Settings: # API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

    # Model Settings
    DEFAULT_MODEL = "gpt-4"
    TEMPERATURE = 0.7
    MAX_TOKENS = 2000

    # Vector Store Settings
    CHROMA_PERSIST_DIR = "./chroma_db"

    @classmethod
    def validate(cls):
        """Validar que las API keys estén configuradas"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY no está configurado en .env")
        return True

## Validar al importar

Settings.validate()
Crear utils básicos - config/utils.py
pythonfrom typing import Any, Dict
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

# 🧪 Paso 6: Test de Configuración

Crear test_setup.py
python"""Test para verificar que todo está configurado correctamente"""
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

if **name** == "**main**":
run_all_tests()

## 🎯 Paso 7: Verificación Final

Ejecutar tests
bashpython test_setup.py
Si todo está bien, deberías ver:

✅ Python version check
✅ OpenAI API Key found
✅ LangChain imports successful
✅ OpenAI Response: Hello World

🚨 Troubleshooting Común
Error: ModuleNotFoundError
bash# Verificar que el entorno virtual esté activado
which python # Debe apuntar a tu entorno virtual

## Reinstalar dependencias

pip install -r requirements.txt
Error: OpenAI API Key

Verificar que .env esté en la raíz del proyecto
Verificar que no haya espacios extra en el API key
Verificar que tengas créditos en tu cuenta OpenAI

Error: Import Error
bash# Actualizar pip
pip install --upgrade pip

## Reinstalar LangChain

pip uninstall langchain langchain-openai
pip install langchain langchain-openai
✅ Checklist Final

Entorno virtual creado y activado
Todas las dependencias instaladas
Archivo .env configurado con API keys
Estructura de carpetas creada
Tests de setup pasando
OpenAI API funcionando

# 🎉 ¡Siguiente Paso!

Una vez que tengas todo configurado, podemos crear tu primer agente básico. ¡Estarás listo para empezar el programa oficial!

⏱️ Tiempo estimado: 30-45 minutos
💡 Tip: Guarda las API keys en un lugar seguro, las usarás durante todo el programa.
