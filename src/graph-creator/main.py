import argparse

from create_graph import create_graph
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

load_dotenv()
# Initialize LLM instances
gpt4 = ChatOpenAI(temperature=0, model_name="gpt-4-turbo")
gemini1_5 = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest")

# Map model names to instances
model_mapping = {
    "gpt": gpt4,
    "gemini": gemini1_5,
}

def main(input_file_path: str, llm_name: str):
    # Read the content of the input file
    try:
        with open(input_file_path, encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file at {input_file_path} was not found.")
        return
    except OSError as e:
        print(f"Error reading file {input_file_path}: {e}")
        return

    # Validate the LLM name
    llm = model_mapping.get(llm_name)
    if llm is None:
        print(f"Error: LLM '{llm_name}' is not recognized. Please choose from {list(model_mapping.keys())}.")
        return

    # Create the graph using the specified LLM
    create_graph(content, llm)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text file content to a graph using a specified LLM.")
    parser.add_argument('input_file_path', type=str, help='Path to the input text file.')
    parser.add_argument('llm_name', type=str, choices=model_mapping.keys(), help='Name of the LLM to use (gpt or gemini).')

    args = parser.parse_args()

    main(args.input_file_path, args.llm_name)
