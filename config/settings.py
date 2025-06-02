import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    
    # Model Settings
    DEFAULT_MODEL = "gpt-4"
    TEMPERATURE = 0.7
    MAX_TOKENS = 2000
    
    @classmethod
    def validate(cls):
        if not cls.OPENAI_API_KEY or cls.OPENAI_API_KEY == "tu_api_key_aqui":
            print("⚠️  OPENAI_API_KEY no configurado en .env")
            return False
        return True
