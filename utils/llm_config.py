import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv(override=True)

# Centralized LLM configuration for the entire enterprise hub
frontier_llm = LLM(
    model="gpt-5.4-mini", 
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.2
)