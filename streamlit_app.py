import streamlit as st
import sys
import os
from dotenv import load_dotenv


#cargo las variables de entorno
load_dotenv()

# Agregar el directorio raíz al path para importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.first_agent import create_agent
from config.settings import Settings
import time

# Configuración de la página
st.set_page_config(
    page_title=" MI Agente de IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #e0e0e0;
    }
    
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    
    .agent-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    
    .tool-info {
        background-color: #fff3e0;
        padding: 0.5rem;
        border-radius: 5px;
        border-left: 3px solid #ff9800;
        margin: 0.5rem 0;
        font-size: 0.9em;
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Inicializar variables de sesión"""
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'agent_initialized' not in st.session_state:
        st.session_state.agent_initialized = False

def display_chat_message(message, is_user=True):
    """Mostrar mensaje en el chat"""
    if is_user:
        st.markdown(f"""
        <div class="chat-message user-message">
            <strong>🧑 Tú:</strong><br>
            {message}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message agent-message">
            <strong>🤖 Agente:</strong><br>
            {message}
        </div>
        """, unsafe_allow_html=True)

def main():
    # Inicializar estado
    initialize_session_state()
    
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>🤖 Mi Primer Agente de IA</h1>
        <p>Chatea con tu agente inteligente que puede hacer cálculos, analizar texto y más</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar con información y configuración
    with st.sidebar:
        st.header("⚙️ Configuración")
        
        # Estado de la API Key
        if Settings.OPENAI_API_KEY and Settings.OPENAI_API_KEY != (os.getenv("OPENAI_API_KEY")):
            st.success("✅ API Key configurada")
            api_status = True
        else:
            st.error("❌ API Key no configurada")
            st.info("Configura tu OpenAI API Key en el archivo .env")
            api_status = False
        
        st.divider()
        
        # Información del agente
        st.header("🔧 Herramientas Disponibles")
        st.markdown("""
        - **Calculadora**: Operaciones matemáticas
        - **Contador de Texto**: Caracteres y palabras
        - **Mayúsculas**: Convertir texto
        """)
        
        st.divider()
        
        # Ejemplos de uso
        st.header("💡 Ejemplos")
        examples = [
            "¿Cuánto es 25 * 4 + 10?",
            "Cuenta las palabras en: 'Hola mundo'",
            "Convierte a mayúsculas: hola mundo",
            "¿Quién eres y qué puedes hacer?"
        ]
        
        for example in examples:
            if st.button(f"📝 {example}", key=f"example_{hash(example)}"):
                if api_status and st.session_state.agent_initialized:
                    st.session_state.messages.append({"user": example, "agent": None})
                    st.rerun()
        
        st.divider()
        
        # Botón para limpiar chat
        if st.button("🗑️ Limpiar Chat"):
            st.session_state.messages = []
            st.rerun()
    
    # Área principal
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Inicializar agente si no está inicializado
        if not st.session_state.agent_initialized and api_status:
            with st.spinner("🤖 Inicializando agente..."):
                try:
                    st.session_state.agent = create_agent()
                    if st.session_state.agent:
                        st.session_state.agent_initialized = True
                        st.success("✅ Agente inicializado correctamente!")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("❌ Error al inicializar el agente")
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
        
        # Mostrar estado del agente
        if not api_status:
            st.warning("⚠️ Configura tu API Key para usar el agente")
        elif not st.session_state.agent_initialized:
            st.info("🔄 Presiona el botón para inicializar el agente")
        else:
            st.success("✅ Agente listo para chatear")
    
    with col2:
        # Información adicional
        st.info("💡 **Tip**: Usa el sidebar para ver ejemplos y herramientas disponibles")
    
    # Área de chat
    st.header("💬 Chat con el Agente")
    
    # Mostrar historial de mensajes
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            display_chat_message(msg["user"], is_user=True)
            if msg["agent"]:
                display_chat_message(msg["agent"], is_user=False)
            elif msg["agent"] is None:
                st.info("⏳ Procesando...")
    
    # Input del usuario
    if st.session_state.agent_initialized:
        user_input = st.chat_input("Escribe tu mensaje aqui...")
        
        if user_input:
            # Agregar mensaje del usuario
            st.session_state.messages.append({"user": user_input, "agent": None})
            
            # Procesar con el agente
            with st.spinner("🤖 El agente está pensando..."):
                try:
                    response = st.session_state.agent.run(user_input)
                    # Actualizar la respuesta del agente
                    st.session_state.messages[-1]["agent"] = response
                except Exception as e:
                    st.session_state.messages[-1]["agent"] = f"❌ Error: {str(e)}"
            
            st.rerun()
    else:
        st.text_input("Mensaje", disabled=True, placeholder="Inicializa el agente primero...")

if __name__ == "__main__":
    main()
    