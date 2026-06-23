import os
from dotenv import load_dotenv
from crewai import Crew, Process
from crews.tech_ops.agents import researcher, inventory_judge, planner
from crews.tech_ops.tasks import telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task

# Environment is loaded and output directory exists
load_dotenv(override=True)
os.makedirs("output", exist_ok=True)

# Build the Crew
aviation_crew = Crew(
    agents=[researcher, inventory_judge, planner],
    tasks=[telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("🛫 Initiating Aviation Multi-Agent System Workflow...")
    
    # Run the system
    result = aviation_crew.kickoff()
    
    print("\n✅ Process Complete. Results exported to output/dispatch_compliance_alert.md")