from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_community.chat_models import ChatOllama
from langchain_classic.hub import pull
from langchain_classic.tools import Tool

# Inicializa el modelo para que se conecte a Ollama localmente
llm = ChatOllama(model="qwen")

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}"

# Envolvemos la función en la clase Tool para que el agente la entienda.
# Esto le añade los atributos .name y .description que el error nos indicaba que faltaban.
tools = [
    Tool(
        name="get_weather",
        func=get_weather,
        description="Use to get the weather for a given city. The input should be the city name.",
    )
]

# Descargamos el prompt compatible para agentes ReAct desde el LangChain Hub.
prompt = pull("hwchase17/react")

# 1. Creamos el agente con el prompt correcto
agent = create_react_agent(llm, tools, prompt)

# 2. Creamos el ejecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

# 3. Invocamos el ejecutor
print(agent_executor.invoke({"input": "As a professional and experienced meteorologist, what is the weather in Maracaibo?"}))
