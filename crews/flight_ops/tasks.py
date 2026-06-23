from crewai import Task
from crews.flight_ops.agents import meteorologist, routing_specialist

def create_flight_ops_tasks(flight_plan: dict):
    
    fetch_weather_task = Task(
        description=f"""
        Use the Open-Meteo tool to check the destination weather for coordinates: 
        Latitude: {flight_plan['dest_lat']}
        Longitude: {flight_plan['dest_lon']}
        
        Generate a concise Aviation Hazard Report. Focus on any conditions that could impact landing safety (e.g., high wind speeds, freezing temperatures, high temperature).
        """,
        expected_output="A short meteorological brief outlining current wind speeds, temperature, and specific aviation hazards.",
        agent=meteorologist
    )

    audit_route_task = Task(
        description=f"""
        Review the Aviation Hazard Report provided by the meteorologist.
        Cross-reference the reported weather against the following operational limits for this specific aircraft:
        
        - Flight: {flight_plan['flight_number']}
        - Tail: {flight_plan['tail_number']}
        - Max Safe Wind Speed: {flight_plan.get('max_wind_kmh', 40)} km/h
        - Minimum Safe Landing Temp: {flight_plan.get('min_temp_c', 0)} °C
        
        Determine if the flight is safe to dispatch and land. 
        Evaluate ALL reported hazards against these specific aircraft limits. If the weather conditions violate ANY of these limits, explicitly flag the flight for a REROUTE or GROUND DELAY.
        """,
        expected_output="A final Go/No-Go Weather Briefing detailing the hazard evaluation, ending with a DISPATCH SIGN-OFF REQUIRED gate.",
        agent=routing_specialist
    )
    
    return [fetch_weather_task, audit_route_task]