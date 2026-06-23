from crewai import Crew, Process
from crews.pax_ops.tasks import create_pax_ops_tasks
from crews.pax_ops.agents import pax_analyst, rebooking_agent

# 1. Define the mock disruption payload (The London Scenario)
mock_disruption = {
    "flight_number": "UA901",
    "disruption_reason": "Severe Crosswinds and Heavy Rain exceeding aircraft operational limits",
    "delay_hours": 6
}

def run_isolated_pax_ops_test():
    print("🚀 [TEST] Initializing Isolated PaxOps Crew Test...")
    
    # 2. Dynamically generate tasks based on the disruption
    pax_ops_tasks = create_pax_ops_tasks(mock_disruption)
    
    # 3. Assemble the crew
    pax_ops_crew = Crew(
        agents=[pax_analyst, rebooking_agent],
        tasks=pax_ops_tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # 4. Kickoff execution
    print("👥 [TEST] Starting Passenger Rebooking Execution...")
    result = pax_ops_crew.kickoff()
    
    print("\n================== 🏁 TEST COMPLETED ==================")
    print("Final Output from Rebooking Specialist:")
    print(result)
    print("=======================================================")

if __name__ == "__main__":
    run_isolated_pax_ops_test()