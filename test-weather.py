from crewai import Crew, Process
from crews.flight_ops.tasks import create_flight_ops_tasks
from crews.flight_ops.agents import meteorologist, routing_specialist

# 1. Define a dynamic mock flight plan payload for London Heathrow (LHR)
mock_flight_plan = {
    "flight_number": "UA901",
    "tail_number": "N789AA",
    "dest_lat": 51.4700,   # London Heathrow Latitude
    "dest_lon": -0.4543,   # London Heathrow Longitude
    "max_wind_kmh": 35,    # Agent will check if live wind exceeds this limit
    "min_temp_c": 5        # Agent will check if live temp falls below this limit
}

def run_isolated_flight_ops_test():
    print("🚀 [TEST] Initializing Isolated FlightOps Crew Test (London Routing)...")
    
    # 2. Dynamically generate the tasks using our mock data
    flight_ops_tasks = create_flight_ops_tasks(mock_flight_plan)
    
    # 3. Assemble the isolated crew
    flight_ops_crew = Crew(
        agents=[meteorologist, routing_specialist],
        tasks=flight_ops_tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # 4. Kickoff the crew execution
    print("🛫 [TEST] Starting Multi-Agent Execution...")
    result = flight_ops_crew.kickoff()
    
    print("\n================== 🏁 TEST COMPLETED ==================")
    print("Final Output from Routing Specialist:")
    print(result)
    print("=======================================================")

if __name__ == "__main__":
    run_isolated_flight_ops_test()