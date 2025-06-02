🔧 Guía de Solución de Problemas - Streamlit IA Agent
🚨 Problemas Más Comunes y Sus Soluciones
1. Error: "API Key no configurada"
bash❌ ERROR: Necesitás configurar tu OpenAI API Key en el archivo .env
Solución:

Crea o edita el archivo .env en la raíz del proyecto:

envOPENAI_API_KEY=tu_api_key_real_aqui
DEFAULT_MODEL=gpt-3.5-turbo
TEMPERATURE=0.7
MAX_TOKENS=1000

Verifica que el archivo .env esté en el mismo directorio que streamlit_app.py
Reinicia Streamlit después de modificar el .env

2. Error: "ModuleNotFoundError"
bashModuleNotFoundError: No module named 'langchain'
Solución:
bash# Activar entorno virtual
source ai-agents-env/bin/activate  # Mac/Linux
# o
ai-agents-env\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Si persiste el error, instalar manualmente:
pip install langchain langchain-openai streamlit python-dotenv rich
3. Error: "ImportError" con módulos locales
bashImportError: cannot import name 'create_agent' from 'agents.first_agent'
Solución:
bash# Ejecutar desde la raíz del proyecto con:
export PYTHONPATH=.:$PYTHONPATH  # Mac/Linux
set PYTHONPATH=.;%PYTHONPATH%    # Windows

# Luego ejecutar Streamlit:
streamlit run streamlit_app.py
4. Error: "Streamlit no se ejecuta"
Solución paso a paso:
bash# 1. Verificar instalación
streamlit --version

# 2. Si no está instalado:
pip install streamlit

# 3. Ejecutar con path completo:
python -m streamlit run streamlit_app.py

# 4. O usar el script:
chmod +x run_streamlit.sh
./run_streamlit.sh
5. Error: "Agent no se inicializa"
Causa común: Problemas con la API Key o conexión
Solución:

Verifica tu saldo en OpenAI: https://platform.openai.com/usage
Prueba tu API Key manualmente:

python# test_api.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello"}],
        max_tokens=10
    )
    print("✅ API Key funciona:", response.choices[0].message.content)
except Exception as e:
    print("❌ Error:", e)
6. Error: "Port already in use"
bashError: Port 8501 is already in use
Solución:
bash# Usar puerto diferente:
streamlit run streamlit_app.py --server.port 8502

# O matar proceso existente (Mac/Linux):
lsof -ti:8501 | xargs kill -9

# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID_NUMBER> /F
🛠️ Script de Diagnóstico Mejorado
Crea un archivo diagnose.py:
pythonimport os
import sys
import subprocess
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
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
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
🚀 Comando de Ejecución Completo
Crea un script mejorado run_app.sh:
bash#!/bin/bash

echo "🚀 Iniciando Aplicación IA Agent..."

# Verificar entorno virtual
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️ Activando entorno virtual..."
    source ai-agents-env/bin/activate 2>/dev/null || {
        echo "❌ Error: Entorno virtual no encontrado"
        echo "Ejecuta: python -m venv ai-agents-env"
        exit 1
    }
fi

# Configurar PYTHONPATH
export PYTHONPATH=".:$PYTHONPATH"

# Verificar dependencias
python -c "import streamlit, langchain, langchain_openai" 2>/dev/null || {
    echo "⚠️ Instalando dependencias faltantes..."
    pip install -r requirements.txt
}

# Verificar .env
if [ ! -f ".env" ]; then
    echo "❌ Archivo .env no encontrado"
    echo "Crea .env con: OPENAI_API_KEY=tu_api_key"
    exit 1
fi

# Ejecutar diagnóstico
echo "🔍 Ejecutando diagnóstico..."
python diagnose.py

echo ""
echo "✅ Iniciando Streamlit..."
echo "🌐 URL: http://localhost:8501"
echo "📱 Para detener: Ctrl+C"

streamlit run streamlit_app.py --server.headless true
📝 Notas Importantes

Siempre ejecuta desde la raíz del proyecto
Activa el entorno virtual antes de ejecutar
Verifica que tu API Key tenga créditos
Si cambias el .env, reinicia Streamlit

🆘 Si Nada Funciona

Reinstalación limpia:

bash# Eliminar entorno virtual
rm -rf ai-agents-env

# Crear nuevo entorno
python -m venv ai-agents-env
source ai-agents-env/bin/activate

# Instalar dependencias una por una
pip install --upgrade pip
pip install streamlit
pip install langchain
pip install langchain-openai
pip install python-dotenv
pip install rich

Prueba versión mínima:

python# minimal_test.py
import streamlit as st
st.write("Hello World!")
bashstreamlit run minimal_test.py