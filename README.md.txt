Conversational AI for Data Exploration
This project implements a question-answering system using large language models (LLMs) to explore data about weightlifting statistics and Olympic medals.

Features
Users can interact with the system through natural language prompts to retrieve information.
Leverages OpenAI's gpt-3.5-turbo-0613 for language processing and generation.
Integrates tools for querying and analyzing data stored in CSV files and PDFs.
Offers a modular architecture for adding new data sources and functionalities.

Usage
Install dependencies: Ensure you have required libraries like pandas, llama-index, and openai installed (refer to their documentation for installation instructions).
Set environment variables: Create a .env file in the project root directory and set any necessary environment variables (e.g., OpenAI API key).
Run the application: Execute main.py to start the system. Users can then enter prompts to interact with the AI.

Data Sources
The system utilizes a CSV file (data/medals.csv) containing Olympic medal data.
Additionally, it leverages a PDF document (data/weightlifting.pdf) providing weightlifting statistics.
Project Structure
main.py: Main script initializing the system and handling user interaction.
note_engine.py: Tool for saving user notes to a text file.
pdf.py: Functions for loading, indexing, and querying PDF data.
prompts.py: Defines templates for prompts used by the LLM.

Technologies
Python
OpenAI API
Pandas
llama-index