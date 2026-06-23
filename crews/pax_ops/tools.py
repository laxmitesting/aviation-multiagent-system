from crewai.tools import BaseTool

class PassengerManifestTool(BaseTool):
    name: str = "Passenger Manifest System"
    description: str = "Retrieves the passenger manifest and connection details for a specific flight number."

    def _run(self, flight_number: str) -> str:
        print(f"\n🗄️ [SYSTEM] Querying CRM for flight {flight_number}...")
        
        # Simulating an enterprise SQL database return
        return f"""
        [MANIFEST DATA FOR {flight_number}]
        - Total Passengers: 142
        - VIP/Frequent Flyers: 12 (Requires immediate concierge rebooking)
        - Connecting Passengers: 45 (Missed connections likely)
        - Unaccompanied Minors: 2
        """