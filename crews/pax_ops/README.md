# 👥 Pax-Ops: Automated Disruption Recovery

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange)](https://github.com/joaomdmoura/crewai)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This module is the **PaxOps** component of the Airline Operational AI Hub. It acts as the downstream safety net in the enterprise architecture, automatically triggering customer recovery workflows when upstream domains (TechOps or FlightOps) flag a flight for grounding or delay.

## 🏗️ System Architecture
This crew utilizes a rapid-triage orchestration pattern to manage passenger logistics, prioritizing high-value and high-risk travelers during operational meltdowns.

`![Architecture Diagram](assets/PaxopsWorkflow.png)`

### The Multi-Agent Workflow
1. **Passenger Manifest Analyst:** Secures access to the simulated CRM database to extract flight manifests. Triages the passenger list to identify VIPs, frequent flyers, unescorted minors, and tight connecting flights.
2. **Rebooking & Compensation Specialist:** Evaluates the triage report against the specific disruption reason and delay duration. Generates an automated, tiered Customer Recovery Plan (including priority rebooking logic and hotel/meal voucher issuance).

## 🛠️ Tech Stack
* **Framework:** CrewAI (Cascading Event Orchestration)
* **LLM Engine:** OpenAI `gpt-5.4-mini` (Centralized Hub Configuration)
* **Tooling:** `PassengerManifestTool` (Simulated Enterprise SQL/CRM integration)
* **Design Pattern:** Downstream Event-Driven Trigger.

## 📂 Component Structure
This crew is architected to receive failure payloads from upstream system evaluations.

```text
crews/pax_ops/
├── agents.py                 # Agent definitions, CRM personas & LLM binding
├── tasks.py                  # Task logic driven by dynamic disruption payloads
└── tools.py                  # Simulated Passenger Manifest Database queries

🚀 Quick Start
Note: This crew is designed to be triggered by a FLIGHT_DISRUPTION_EVENT from the root orchestrator.

Ensure environment variables (OPENAI_API_KEY) are set in the project root .env file.

To test the recovery logic in isolation, execute from the root directory:

Bash
python test_pax.py


To test the cascading enterprise pipeline, execute:

Bash
python main_orchestrator.py


☁️ Production Roadmap
GDS Integration: Connect the Rebooking Specialist directly to Sabre or Amadeus APIs for live seat reservations.

Automated Comms: Integrate SendGrid/Twilio APIs to auto-text meal vouchers and new boarding passes directly to passenger phones.

Sentiment Analysis: Parse live Twitter/X data for the specific flight to prioritize outreach to visibly frustrated VIPs.

