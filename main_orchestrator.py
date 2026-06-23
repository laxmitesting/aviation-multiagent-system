from crewai import Crew, Process

# --- 1. TechOps Imports ---
from crews.tech_ops.agents import researcher, inventory_judge, planner
from crews.tech_ops.tasks import telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task 

# --- 2. FlightOps Imports ---
from crews.flight_ops.agents import meteorologist, routing_specialist
from crews.flight_ops.tasks import create_flight_ops_tasks

# --- 3. PaxOps Imports ---
from crews.pax_ops.agents import pax_analyst, rebooking_agent
from crews.pax_ops.tasks import create_pax_ops_tasks

# ==============================================================================
# CREW TRIGGERS (The "Spokes")
# ==============================================================================

def trigger_tech_ops_crew():
    print("\n⚙️ [HUB] Waking up TechOps Crew (Maintenance Compliance)...")
    tech_ops_crew = Crew(
        agents=[researcher, inventory_judge, planner],
        tasks=[telemetry_analysis_task, inventory_validation_task, maintenance_scheduling_task],
        process=Process.sequential,
        verbose=True
    )
    return tech_ops_crew.kickoff()

def trigger_flight_ops_crew(payload):
    print("\n🌤️ [HUB] Waking up FlightOps Crew (Weather & Routing)...")
    tasks = create_flight_ops_tasks(payload)
    flight_ops_crew = Crew(
        agents=[meteorologist, routing_specialist],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    return flight_ops_crew.kickoff()

def trigger_pax_ops_crew(payload):
    print("\n👥 [HUB] Waking up PaxOps Crew (Passenger Rebooking & Recovery)...")
    tasks = create_pax_ops_tasks(payload)
    pax_ops_crew = Crew(
        agents=[pax_analyst, rebooking_agent],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    return pax_ops_crew.kickoff()

# ==============================================================================
# API GATEWAY (The "Hub")
# ==============================================================================

def global_event_router(event_type: str, payload: dict = None):
    """
    Routes incoming events to isolated domain crews.
    """
    print(f"\n📡 [API GATEWAY] Incoming Event Detected: {event_type}")
    
    if event_type == "MAINTENANCE_AUDIT_REQUEST":
        return trigger_tech_ops_crew()
        
    elif event_type == "FLIGHT_FILED_WEATHER_CHECK":
        return trigger_flight_ops_crew(payload)
        
    elif event_type == "FLIGHT_DISRUPTION_EVENT":
        return trigger_pax_ops_crew(payload)
        
    else:
        return f"ERROR: Unrecognized event type: {event_type}"

# ==============================================================================
# SIMULATED EVENT TRIGGERS (For Portfolio Demonstration)
# ==============================================================================
if __name__ == "__main__":
    print("🛫 INITIALIZING AIRLINE OPERATIONAL AI HUB...\n")
    
    # --- TEST 1: TechOps Batch Process ---
    # global_event_router("MAINTENANCE_AUDIT_REQUEST")
    
    # --- TEST 2: FlightOps Weather Check ---
    # mock_london_flight = {"flight_number": "UA901", "tail_number": "N789AA", "dest_lat": 51.4700, "dest_lon": -0.4543, "max_wind_kmh": 35, "min_temp_c": 5}
    # global_event_router("FLIGHT_FILED_WEATHER_CHECK", payload=mock_london_flight)
    
    # --- TEST 3: PaxOps Disruption Recovery ---
    mock_disruption = {
        "flight_number": "UA901",
        "disruption_reason": "Severe Crosswinds and Heavy Rain exceeding aircraft operational limits",
        "delay_hours": 6
    }
    
    # This will trigger the PaxOps workflow directly from the global orchestrator!
    pax_ops_result = global_event_router("FLIGHT_DISRUPTION_EVENT", payload=mock_disruption)
    print("\n--- FINAL PAXOPS RECOVERY PLAN ---")
    print(pax_ops_result)