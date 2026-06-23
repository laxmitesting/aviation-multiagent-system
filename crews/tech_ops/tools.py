import json
import os
import time
from crewai.tools import BaseTool

class MROInventoryTool(BaseTool):
    name: str = "MRO Inventory Database Tool"
    description: str = "Simulates looking up an aircraft's live maintenance constraints. Requires the aircraft tail number as input (e.g., 'N104HX')."

    def _run(self, tail_number: str) -> str:
        print(f"\n⏳ [SYSTEM] Accessing Secure MRO Database for {tail_number}...")
        time.sleep(3) 
        print("✅ [SYSTEM] Data retrieved. Returning to Agent...\n")
        
        file_path = 'data/mro_inventory.json'
        
        if not os.path.exists(file_path):
            return "ERROR: Registry database offline or file not found."
            
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            registry = data.get("registry", {})
            
            if tail_number in registry:
                return str(registry[tail_number]) # Pydantic prefers string outputs
            return "UNKNOWN_TAIL_NOT_IN_REGISTRY"
            
        except json.JSONDecodeError:
            return "ERROR: Database file is corrupted."