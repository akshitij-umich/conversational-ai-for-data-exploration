from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
from pdf import weightlifting_engine

load_dotenv()

medals_path = os.path.join("data", "medals.csv")
medals_df = pd.read_csv(medals_path)

medals_query_engine = PandasQueryEngine(
    df=medals_df, verbose=True, instruction_str=instruction_str
)
medals_query_engine.update_prompts({"pandas_prompt": new_prompt})

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=medals_query_engine,
        metadata=ToolMetadata(
            name="medals_data",
            description="this gives information at the olympics and medals",
        ),
    ),
    QueryEngineTool(
        query_engine=weightlifting_engine,
        metadata=ToolMetadata(
            name="weightlifting_data",
            description="this gives detailed information about weightlifting the sport",
        ),
    ),
]

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)