import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
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

# Validar al importar
Settings.validate()
