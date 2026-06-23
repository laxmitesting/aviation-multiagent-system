import requests
from crewai.tools import BaseTool

class OpenMeteoTool(BaseTool):
    name: str = "Open-Meteo Aviation Weather API"
    description: str = "Fetches global weather data. Requires latitude and longitude."

    def _run(self, lat: float, lon: float) -> str:
        print(f"\n📡 [SYSTEM] Pinging Open-Meteo for coordinates: {lat}, {lon}...")
        
        # Open-Meteo v1 forecast endpoint for current temperature and wind speed
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m,weather_code"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Extract current conditions
            current = data.get('current', {})
            wind_speed = current.get('wind_speed_10m', 0)
            temp = current.get('temperature_2m', 0)
            
            # Basic logical parser to assist the Meteorologist Agent
            hazards = []
            if wind_speed > 40: 
                hazards.append("SEVERE_CROSSWINDS")
            if temp < 0: 
                hazards.append("ICING_CONDITIONS_EXPECTED")
            
            if not hazards:
                return f"Weather Clear at {lat},{lon}. Wind: {wind_speed}km/h, Temp: {temp}C."
                
            return f"HAZARD DETECTED at {lat},{lon}: {', '.join(hazards)}. Wind: {wind_speed}km/h, Temp: {temp}C."
            
        except requests.exceptions.RequestException as e:
            return f"ERROR: Weather API unreachable. Details: {e}"