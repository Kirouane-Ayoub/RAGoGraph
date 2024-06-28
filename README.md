# RAGoGraph

```
██████   █████   ██████   ██████   ██████  ██████   █████  ██████  ██   ██ 
██   ██ ██   ██ ██       ██    ██ ██       ██   ██ ██   ██ ██   ██ ██   ██ 
██████  ███████ ██   ███ ██    ██ ██   ███ ██████  ███████ ██████  ███████ 
██   ██ ██   ██ ██    ██ ██    ██ ██    ██ ██   ██ ██   ██ ██      ██   ██ 
██   ██ ██   ██  ██████   ██████   ██████  ██   ██ ██   ██ ██      ██   ██ 
                                                                           
                              Graph QA Chatbot
                              🦜🔗 langchain                                            
```

**RAGoGraph** is a project designed to seamlessly convert text into a **knowledge graph** and leverage this structured data within a conversational agent. The project is divided into two main components. 

The first component focuses on transforming given textual data into a knowledge graph and storing it in a **Neo4j database**. 

The second component utilizes the **🦜🔗 LangChain framework** to develop an intelligent **conversational agent**, which interacts with the knowledge graph stored in Neo4j. 

**Streamlit** is employed as the user interface library, providing an interactive and user-friendly front end. This setup allows for dynamic and insightful conversations, as the agent can query and retrieve information from the knowledge graph, enhancing the user's experience with rich, context-aware responses.
                                                                         
## Requirements

- Python 3.8+
- Install dependencies from `requirements.txt`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Kirouane-Ayoub/RAGoGraph.git
    cd RAGoGraph
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:
    ```ini
    NEO4J_URI=........
    NEO4J_USERNAME=neo4j
    NEO4J_PASSWORD=........
    AURA_INSTANCEID=........
    AURA_INSTANCENAME=........
    OPENAI_API_KEY=........
    GOOGLE_API_KEY=........
    ```
5. create the graph from you data and store it in neo4j : 

    ```sh
    python src/graph-creator/main.py data.txt gemini # or gpt4
    ```
6. Run the streamlit app : 
    ```sh
    streamlit run src/graph-rag/app.py
    ```
  ![Screenshot from 2024-06-21 19-10-27](https://github.com/Kirouane-Ayoub/RAGoGraph/assets/99510125/f73b484c-45bb-4077-8fb2-6cc67ab08502)

## Integration with LangSmith

You can integrate LangSmith for tracking your project by adding the following lines to your `.env` file:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<your-api-key>"
```

### LangSmith

LangSmith is an all-in-one developer platform for every step of the LLM-powered application lifecycle, whether you’re building with LangChain or not. It allows you to debug, collaborate, test, and monitor your LLM applications effectively.
