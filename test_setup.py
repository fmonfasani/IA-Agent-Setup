# -*- coding: utf-8 -*-
"""Test para verificar que todo esta configurado correctamente"""
import os
import sys

def test_environment():
    """Verificar entorno Python"""
    print("\n Testing Python Environment...")
    print(f"Python version: {sys.version}")
    print(f"Current directory: {os.getcwd()}")
    
def test_imports():
    """Test imports basicos"""
    print("\n Testing Basic Imports...")
    
    try:
        import dotenv
        print("OK python-dotenv installed")
    except ImportError:
        print("ERROR python-dotenv not installed")
        
    try:
        from config.settings import Settings
        print("OK Settings imported successfully")
    except ImportError as e:
        print(f"ERROR Settings import failed: {e}")

def test_api_keys():
    """Verificar API keys"""
    print("\n Testing API Keys...")
    
    if os.path.exists('.env'):
        print("OK .env file exists")
        
        try:
            from config.settings import Settings
            if Settings.OPENAI_API_KEY and Settings.OPENAI_API_KEY != "tu_api_key_aqui":
                print("OK OpenAI API Key configured")
            else:
                print("WARNING OpenAI API Key not configured")
        except:
            print("ERROR reading settings")
    else:
        print("ERROR .env file not found")

def run_all_tests():
    """Ejecutar todos los tests"""
    print("Starting Environment Setup Tests")
    
    test_environment()
    test_imports() 
    test_api_keys()
    
    print("\nSetup tests completed!")
    print("\nNext steps:")
    print("1. Configure your OpenAI API key in .env file")
    print("2. Install dependencies: pip install langchain langchain-openai")

if __name__ == "__main__":
    run_all_tests()
