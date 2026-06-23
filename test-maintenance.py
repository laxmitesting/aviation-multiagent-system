from crewai import Crew, Process

# Import the correct pre-configured agents and tasks
from crews.tech_ops.agents import researcher, inventory_judge, planner
from crews.tech_ops.tasks import telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task

def run_isolated_tech_ops_test():
    print("🚀 [TEST] Initializing Isolated TechOps Crew Test (Batch Processing)...")
    
    # 1. Assemble the isolated crew with the correct task names
    tech_ops_crew = Crew(
        agents=[researcher, inventory_judge, planner],
        tasks=[telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task],
        process=Process.sequential,
        verbose=True
    )
    
    # 2. Kickoff execution
    print("⚙️ [TEST] Starting Maintenance Sweep Execution...")
    print("   -> Note: The Flight Safety Analyst is reading from data/mock_telemetry.csv")
    result = tech_ops_crew.kickoff()
    
    print("\n================== 🏁 TEST COMPLETED ==================")
    print("Final Output from Line Mechanic Foreman:")
    print(result)
    print("=======================================================")

if __name__ == "__main__":
    run_isolated_tech_ops_test()