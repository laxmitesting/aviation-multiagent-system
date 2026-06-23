from crewai import Task
from crews.tech_ops.tools import MROInventoryTool
from crews.tech_ops.agents import researcher, inventory_judge, planner

# Task 1: Find plans pending approval
telemetry_analysis_task = Task(
    description=(
        "Scan the local CSV file (data/mock_telemetry.csv). "
        "Locate flight entries where the status is currently marked as 'PENDING'. "
        "Extract the flight number, the aircraft tail number, and the full string of "
        "filed_equipment_codes and filed_surveillance_codes."
    ),
    expected_output=(
        "A Markdown brief summarizing pending flights, specifically noting the tail number "
        "and their requested operational equipment codes."
    ),
    agent=researcher
)

# Task 2: Cross-reference filed codes against the physical registry truth
inventory_validation_task = Task(
    description=(
        "Cross-reference the pending flight codes with the official avionics registry "
        "contained in (data/mro_inventory.json). Audit whether the aircraft's physical status "
        "supports the filed codes. Identify if a flight is filing code 'G' or 'B' (GPS/LPV) "
        "while the aircraft registry shows a 'GPS_DEGRADED' status."
    ),
    expected_output=(
        "An avionics discrepancy report highlighting any equipment mismatches, "
        "flagging 'COMPLIANT' or 'MISMATCH_RISK'."
    ),
    agent=inventory_judge,
)

# Task 3: Generate the Flight Dispatch Alert & Correction Notice
maintenance_scheduling_task = Task(
    description=(
        "Take the discrepancy report and compile an official Flight Dispatch Compliance Alert. "
        "If an equipment code violation is flagged, draft a revised, compliant set of equipment codes . "         
        "for the dispatcher. Conclude with a clear 'DISPATCH SIGN-OFF REQUIRED' gate."
    ),
    expected_output=(
        "A formal flight dispatch compliance document in Markdown format, "
        "detailing safety flag warnings and recommended equipment code corrections."
    ),
    agent=planner,
    output_file="output/dispatch_compliance_alert.md"
)
