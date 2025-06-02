import os
import sys
from pathlib import Path

def check_environment():
    print("🔍 DIAGNÓSTICO DEL ENTORNO")
    print("=" * 50)
    
    # Python version
    print(f"Python: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    
    # Virtual environment
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Entorno virtual activo")
    else:
        print("⚠️ No se detectó entorno virtual")
    
    # Required files
    files_to_check = ['.env', 'streamlit_app.py', 'agents/first_agent.py', 'config/settings.py']
    for file in files_to_check:
        if Path(file).exists():
            print(f"✅ {file} existe")
        else:
            print(f"❌ {file} falta")
    
    # Dependencies
    required_packages = ['streamlit', 'langchain', 'langchain_openai', 'python-dotenv']
    
    module_names = {
        'streamlit': 'streamlit',
        'langchain': 'langchain',
        'langchain_openai': 'langchain_openai',
        'python-dotenv': 'dotenv',  # <- Corrigiendo el nombre del módulo
    }

    for package in required_packages:
        module_name = module_names.get(package, package.replace('-', '_'))
        try:
            __import__(module_name)
            print(f"✅ {package} instalado")
        except ImportError:
            print(f"❌ {package} no instalado")
    
    # API Key
    try:
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key and len(api_key) > 10:
            print(f"✅ API Key configurada ({api_key[:8]}...)")
        else:
            print("❌ API Key no configurada o inválida")
    except Exception as e:
        print(f"❌ Error leyendo .env: {e}")

if __name__ == "__main__":
    check_environment()
