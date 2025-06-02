import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Settings:
    """Configuración centralizada para el proyecto IA Agent"""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-3.5-turbo")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1000"))
    
    # Paths
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEMORY_PATH = os.path.join(PROJECT_ROOT, "memory")
    TOOLS_PATH = os.path.join(PROJECT_ROOT, "tools")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def validate(cls):
        """Validar configuración crítica"""
        if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == "tu_clave_openai_aqui":
            print("❌ ERROR: Necesitás configurar tu OpenAI API Key en el archivo .env")
            print("   Editá .env y agregá: OPENAI_API_KEY=tu_clave_real")
            return False
        
        if not os.path.exists(cls.MEMORY_PATH):
            os.makedirs(cls.MEMORY_PATH, exist_ok=True)
            
        if not os.path.exists(cls.TOOLS_PATH):
            os.makedirs(cls.TOOLS_PATH, exist_ok=True)
            
        return True
    
    @classmethod
    def show_config(cls):
        """Mostrar configuración actual (sin mostrar la API key completa)"""
        api_key_display = f"{cls.OPENAI_API_KEY[:8]}..." if cls.OPENAI_API_KEY else "No configurada"
        
        print("🔧 Configuración actual:")
        print(f"   API Key: {api_key_display}")
        print(f"   Modelo: {cls.DEFAULT_MODEL}")
        print(f"   Temperatura: {cls.TEMPERATURE}")
        print(f"   Max Tokens: {cls.MAX_TOKENS}")
        print(f"   Directorio raíz: {cls.PROJECT_ROOT}")