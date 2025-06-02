# -*- coding: utf-8 -*-
"""
Tu primer agente de IA funcional
Un agente simple que puede responder preguntas y usar herramientas basicas
"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from config.settings import Settings
import math

def calculator_tool(expression: str) -> str:
    """Calculadora basica que evalua expresiones matematicas"""
    try:
        # Por seguridad, solo permite operaciones basicas
        allowed_chars = set('0123456789+-*/.() ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Solo se permiten numeros y operaciones basicas"
        
        result = eval(expression)
        return f"El resultado es: {result}"
    except Exception as e:
        return f"Error en el calculo: {str(e)}"

def length_tool(text: str) -> str:
    """Cuenta caracteres y palabras en un texto"""
    char_count = len(text)
    word_count = len(text.split())
    return f"El texto tiene {char_count} caracteres y {word_count} palabras"

def upper_tool(text: str) -> str:
    """Convierte texto a mayusculas"""
    return text.upper()

def create_agent():
    """Crear y configurar el agente"""
    
    # Verificar configuracion
    if not Settings.validate():
        print("ERROR: Configura tu OpenAI API Key en el archivo .env")
        return None
    
    # Inicializar el modelo LLM
    llm = ChatOpenAI(
        model=Settings.DEFAULT_MODEL,
        temperature=Settings.TEMPERATURE,
        openai_api_key=Settings.OPENAI_API_KEY
    )
    
    # Definir herramientas disponibles
    tools = [
        Tool(
            name="Calculadora",
            func=calculator_tool,
            description="Usar para calculos matematicos. Input: expresion matematica como '2+2' o '10*5'"
        ),
        Tool(
            name="Contador_Texto",
            func=length_tool,
            description="Contar caracteres y palabras en un texto. Input: el texto a analizar"
        ),
        Tool(
            name="Mayusculas",
            func=upper_tool,
            description="Convertir texto a mayusculas. Input: texto a convertir"
        )
    ]
    
    # Memoria para recordar la conversacion
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Crear el agente
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True,  # Para ver el proceso de pensamiento
        handle_parsing_errors=True
    )
    
    return agent

def chat_with_agent():
    """Función principal para chatear con el agente"""
    
    print("🤖 Iniciando tu primer agente de IA...")
    print("=" * 50)
    
    # Crear el agente
    agent = create_agent()
    if not agent:
        return
    
    print("✅ Agente creado exitosamente!")
    print("\n🔧 Herramientas disponibles:")
    print("- Calculadora (para matematicas)")
    print("- Contador de texto (caracteres y palabras)")
    print("- Convertir a mayusculas")
    
    print("\n💬 Ejemplos de preguntas:")
    print("- 'Cuanto es 25 * 4 + 10?'")
    print("- 'Cuantas palabras tiene este texto: Hola mundo'")
    print("- 'Convierte esta frase a mayusculas: hola mundo'")
    print("- 'Quien eres y que puedes hacer?'")
    
    print("\n" + "=" * 50)
    print("Escribe 'salir' para terminar")
    print("=" * 50)
    
    while True:
        try:
            # Obtener input del usuario
            user_input = input("\n🧑 Tu: ").strip()
            
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("\n👋 ¡Hasta luego!")
                break
                
            if not user_input:
                print("Por favor escribe algo...")
                continue
            
            # Ejecutar el agente
            print(f"\n🤖 Agente pensando...")
            response = agent.run(user_input)
            print(f"\n🤖 Agente: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Conversacion interrumpida. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Intenta de nuevo...")

def test_agent():
    """Función para probar el agente automaticamente"""
    print("🧪 Probando el agente automaticamente...")
    
    agent = create_agent()
    if not agent:
        return
    
    test_questions = [
        "Hola, quien eres?",
        "Cuanto es 15 + 27?",
        "Cuantas palabras tiene: 'Python es genial para IA'",
        "Convierte a mayusculas: 'mi primer agente'"
    ]
    
    for question in test_questions:
        print(f"\n🧑 Pregunta: {question}")
        try:
            response = agent.run(question)
            print(f"🤖 Respuesta: {response}")
        except Exception as e:
            print(f"❌ Error: {e}")
        print("-" * 40)

if __name__ == "__main__":
    print("Selecciona una opcion:")
    print("1. Chat interactivo con el agente")
    print("2. Prueba automatica")
    
    choice = input("Opcion (1 o 2): ").strip()
    
    if choice == "1":
        chat_with_agent()
    elif choice == "2":
        test_agent()
    else:
        print("Opcion invalida. Ejecutando chat interactivo...")
        chat_with_agent()