# Mini Proyecto: Agente Local con LangChain y Ollama

Este es un proyecto de demostración simple que muestra cómo construir y ejecutar un agente conversacional de LangChain utilizando un modelo de lenguaje de código abierto (`Qwen`) que se ejecuta 100% localmente a través de Ollama.

El agente tiene acceso a una herramienta simple para "consultar" el clima de una ciudad y es capaz de razonar sobre cuándo usarla para responder a las preguntas del usuario.

## Tecnologías Utilizadas

*   **Python 3**
*   **LangChain**: Framework para el desarrollo de aplicaciones con modelos de lenguaje.
    *   Se utiliza `langchain-classic` para la creación de un agente robusto de tipo "ReAct".
*   **Ollama**: Herramienta para ejecutar modelos de lenguaje de código abierto de forma local.
*   **Qwen**: El modelo de lenguaje de Alibaba que se ejecuta en Ollama.

## Requisitos Previos

Antes de empezar, asegúrate de tener instalado lo siguiente en tu sistema:

1.  **Python 3.10+**
2.  **Ollama**: Puedes descargarlo e instalarlo desde [ollama.com](https://ollama.com/).

## Instalación

Sigue estos pasos para configurar el entorno y poner en marcha el proyecto:

1.  **Clonar el Repositorio**
    (Si aún no tienes los archivos en tu máquina local).

2.  **Crear y Activar un Entorno Virtual**
    Es una buena práctica aislar las dependencias del proyecto.
    ```bash
    # Crear el entorno virtual
    python3 -m venv .venv

    # Activar el entorno (en Linux/macOS)
    source .venv/bin/activate
    ```

3.  **Instalar las Dependencias**
    Instala todas las librerías de Python necesarias con el siguiente comando:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Descargar el Modelo de Ollama**
    Este comando descarga el modelo `qwen` para que Ollama pueda utilizarlo.
    ```bash
    ollama pull qwen
    ```

## Uso

1.  **Asegúrate de que Ollama esté Corriendo**
    El servicio de Ollama debe estar activo. Si no lo está, puedes iniciarlo abriendo una terminal y ejecutando:
    ```bash
    ollama serve
    ```
    > **Nota**: Si recibes un error como `address already in use`, ¡es una buena noticia! Significa que Ollama ya se está ejecutando en segundo plano.

2.  **Ejecutar el Script Principal**
    Con el entorno virtual activado, ejecuta el siguiente comando:
    ```bash
    python main.py
    ```

3.  **Salida Esperada**
    Gracias a la opción `verbose=True`, verás el "razonamiento" del agente en la terminal antes de dar la respuesta final. La salida se verá similar a esto:

    ```
    > Entering new AgentExecutor chain...
    I need to find out the weather in Maracaibo. I have a tool for that.
    Action: get_weather
    Action Input: Maracaibo
    Observation: It's always sunny in Maracaibo
    I now know the final answer.
    Final Answer: The weather in Maracaibo is always sunny.

    > Finished chain.
    {'input': 'As a professional and experienced meteorologist, what is the weather in Maracaibo?', 'output': 'The weather in Maracaibo is always sunny.'}
    ```
