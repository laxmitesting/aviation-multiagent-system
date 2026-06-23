from crewai import Agent
from utils.llm_config import frontier_llm
from crews.pax_ops.tools import PassengerManifestTool

pax_analyst = Agent(
    role="Passenger Manifest Analyst",
    goal="Analyze flight manifests to identify high-risk or VIP passengers during a disruption.",
    backstory="You are an expert in customer relationship management. You quickly triage passenger lists to see who will miss connections.",
    tools=[PassengerManifestTool()],
    llm=frontier_llm,
    verbose=True
)

rebooking_agent = Agent(
    role="Rebooking & Compensation Specialist",
    goal="Draft an automated rebooking strategy and compensation plan for disrupted flights.",
    backstory="You are a senior customer service agent. You create equitable rebooking plans and issue meal/hotel vouchers based on the delay duration.",
    tools=[], 
    llm=frontier_llm,
    verbose=True
)