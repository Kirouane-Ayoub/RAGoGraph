# RAGoGraph

```
██████   █████   ██████   ██████   ██████  ██████   █████  ██████  ██   ██ 
██   ██ ██   ██ ██       ██    ██ ██       ██   ██ ██   ██ ██   ██ ██   ██ 
██████  ███████ ██   ███ ██    ██ ██   ███ ██████  ███████ ██████  ███████ 
██   ██ ██   ██ ██    ██ ██    ██ ██    ██ ██   ██ ██   ██ ██      ██   ██ 
██   ██ ██   ██  ██████   ██████   ██████  ██   ██ ██   ██ ██      ██   ██ 
                                                                           
                              Graph QA Chatbot                                             
```                                                                          
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
