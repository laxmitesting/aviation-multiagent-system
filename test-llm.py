# %%
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

# 1. Load your API key
load_dotenv(override=True)

print("🔌 Connecting to the frontier model...")
frontier_llm = LLM(
    model="gpt-5.4-mini", 
    api_key=os.getenv("OPENAI_API_KEY")
)

# 2. Create a bare-minimum test agent
test_agent = Agent(
    role="Comm Check Agent",
    goal="Verify the API connection is working.",
    backstory="You are a simple diagnostic tool.",
    llm=frontier_llm
)

# 3. Give it a simple, isolated task
test_task = Task(
    description="Write a one-sentence radio check confirming that the OpenAI model is active and responding.",
    expected_output="A single sentence confirmation.",
    agent=test_agent
)

# 4. Run the test
print("🚀 Firing test prompt to the API...\n")
test_crew = Crew(agents=[test_agent], tasks=[test_task])
result = test_crew.kickoff()

print("\n✅ === MODEL RESPONSE ===")
print(result)