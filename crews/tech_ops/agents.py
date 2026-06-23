from crewai import Agent
from crewai_tools import FileReadTool   
from crews.tech_ops.tools import MROInventoryTool
from utils.llm_config import frontier_llm

telemetry_csv_tool = FileReadTool(file_path='data/mock_telemetry.csv')

researcher = Agent(
    role='Flight Safety Data Analyst',
    goal='Analyze telemetry logs for anomaly patterns matching ATA chapters',
    backstory='You are an expert in parsing flight data logs and identifying thermal anomalies.',
    tools=[telemetry_csv_tool],
    llm=frontier_llm, 
    verbose=True
)

inventory_judge = Agent(
    role="Hangar Inventory Manager",
    goal="Verify part availability...",
    backstory="You are a veteran maintenance manager...",
    llm=frontier_llm,
    tools=[MROInventoryTool()] 
)

planner = Agent(
    role='Line Mechanic Foreman',
    goal='Generate proactive work orders and request Human-in-the-Loop approval',
    backstory='You coordinate maintenance schedules to minimize Aircraft on Ground (AOG) hours.',
    llm=frontier_llm, 
    verbose=True
)