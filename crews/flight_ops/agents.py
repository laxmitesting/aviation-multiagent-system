from crewai import Agent
from utils.llm_config import frontier_llm
from crews.flight_ops.tools import OpenMeteoTool

meteorologist = Agent(
    role="Aviation Meteorologist",
    goal="Pull global weather data for flight routes and generate hazard reports.",
    backstory="You are a veteran atmospheric scientist. You strictly report facts based on Open-Meteo data without making operational routing decisions.",
    tools=[OpenMeteoTool()],
    llm=frontier_llm,
    verbose=True
)

routing_specialist = Agent(
    role="Flight Routing Specialist",
    goal="Reconcile weather hazards with filed aircraft capabilities.",
    backstory="You are a meticulous flight dispatcher. You compare weather hazard reports against the equipment limitations of the filed aircraft to ensure safety compliance.",
    tools=[], # The routing rules are passed in via the task parameters
    llm=frontier_llm,
    verbose=True
)