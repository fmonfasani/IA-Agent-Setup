#!/bin/bash

# Script para ejecutar la aplicación Streamlit
echo "🚀 Iniciando aplicación web del Agente IA..."

# Verificar que el entorno virtual esté activado
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️ ADVERTENCIA: No se detectó un entorno virtual activo"
    echo "   Asegúrate de activar tu entorno virtual primero:"
    echo "   - Windows: ai-agents-env\\Scripts\\activate"
    echo "   - Mac/Linux: source ai-agents-env/bin/activate"
    echo ""
fi

# Verificar que Streamlit esté instalado
if ! command -v streamlit &> /dev/null; then
    echo "❌ Streamlit no está instalado"
    echo "   Instálalo con: pip install streamlit"
    exit 1
fi

# Verificar archivo .env
if [ ! -f ".env" ]; then
    echo "❌ Archivo .env no encontrado"
    echo "   Crea el archivo .env con tu OpenAI API Key"
    exit 1
fi

# Configurar variables de entorno
export PYTHONPATH=".:$PYTHONPATH"

echo "✅ Iniciando aplicación Streamlit..."
echo "   La aplicación se abrirá en: http://localhost:8501"
echo "   Presiona Ctrl+C para detener la aplicación"
echo ""

# Ejecutar Streamlit
streamlit run streamlit_app.py