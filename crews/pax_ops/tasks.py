from crewai import Task
from crews.pax_ops.agents import pax_analyst, rebooking_agent

def create_pax_ops_tasks(disruption_payload: dict):
    
    triage_task = Task(
        description=f"""
        Use the Passenger Manifest System to pull data for Flight: {disruption_payload['flight_number']}.
        
        Identify the breakdown of passengers impacted by the following disruption:
        Reason: {disruption_payload['disruption_reason']}
        Delay Duration: {disruption_payload['delay_hours']} hours.
        """,
        expected_output="A triage report detailing total passengers impacted, with special emphasis on VIPs and connecting flights.",
        agent=pax_analyst
    )

    compensation_task = Task(
        description=f"""
        Review the triage report. Based on the delay duration of {disruption_payload['delay_hours']} hours, generate a Customer Recovery Plan.
        
        The plan must include:
        1. Priority rebooking instructions for VIPs and Minors.
        2. Mass-rebooking logic for standard passengers.
        3. Compensation tiers (e.g., if delay > 4 hours, issue meal vouchers; if overnight, issue hotel vouchers).
        """,
        expected_output="A structured Customer Recovery Action Plan ready to be emailed to the airport gate agents.",
        agent=rebooking_agent
    )
    
    return [triage_task, compensation_task]