from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer


def create_graph(text,llm):
    # Load environment variables
    load_dotenv()
    # Initialize the Neo4j graph
    graph = Neo4jGraph()

    # Initialize the LLM for graph transformation
    llm_transformer = LLMGraphTransformer(llm=llm)

    # Convert the text to a Document object
    documents = [Document(page_content=text)]

    # Transform the document into graph documents
    graph_documents = llm_transformer.convert_to_graph_documents(documents)

    # Add the graph documents to the Neo4j graph
    graph.add_graph_documents(graph_documents)


