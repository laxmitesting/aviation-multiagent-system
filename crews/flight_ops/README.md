# 🌤️ Flight-Ops: Dynamic Weather & Routing Optimization

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange)](https://github.com/joaomdmoura/crewai)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This module is the **FlightOps** component of the Airline Operational AI Hub. It is an event-driven, multi-agent orchestration pipeline designed to pull real-time global weather data and strictly evaluate it against specific aircraft operational limits (e.g., maximum crosswind tolerances, minimum landing temperatures).

## 🏗️ System Architecture
This crew utilizes a sequential orchestration pattern to dynamically evaluate environmental hazards before flight dispatch.

`![Architecture Diagram](assets/FlightOpsWorkflow.png)`

### The Multi-Agent Workflow
1. **Aviation Meteorologist:** Pings the Open-Meteo REST API using destination coordinates to pull real-time wind speed, temperature, and atmospheric data, translating it into an Aviation Hazard Report.
2. **Flight Routing Specialist:** Synthesizes the hazard report against the payload's specific aircraft limits (e.g., tail number limitations, anti-ice capabilities) and acts as the Go/No-Go gate, flagging flights for REROUTE or GROUND DELAY if safety thresholds are breached.

## 🛠️ Tech Stack
* **Framework:** CrewAI (Event-Driven Task Orchestration)
* **LLM Engine:** OpenAI `gpt-5.4-mini` (Centralized Hub Configuration)
* **Tooling:** `OpenMeteoTool` (Custom Python API wrapper for global coordinate weather extraction)
* **Architecture:** Rules-Engine evaluation pattern.

## 📂 Component Structure
This crew is architected as an isolated, event-driven module within the global Airline Operational AI Hub.

```text
crews/flight_ops/
├── agents.py                 # Agent definitions, personas & LLM binding
├── tasks.py                  # Dynamic task logic requiring JSON payload injections
└── tools.py                  # Custom Open-Meteo API integration


🚀 Quick Start
Note: This crew is intended to be triggered by the root-level global orchestrator, but can be tested in isolation.

Ensure environment variables (OPENAI_API_KEY) are set in the project root .env file.

To test in isolation, execute from the root directory:

Bash
python test_weather.py


To run as part of the enterprise pipeline, execute:

Bash
python main_orchestrator.py


☁️ Production Roadmap
Aviation API Integration: Upgrade from Open-Meteo to strict FAA/NOAA METAR/TAF XML feeds.

Fuel Recalculation: Add a Dispatch Agent to calculate holding-pattern fuel reserves if a ground delay is flagged.

Live Geospatial Mapping: Output flagged routes to a Mapbox/Google Maps interactive dashboard.

