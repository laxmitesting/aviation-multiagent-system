✈️ Tech-Ops: Automated Dispatch Compliance

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange)](https://github.com/joaomdmoura/crewai)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This module is the TechOps component of the Airline Operational AI Hub. It is an enterprise-grade, multi-agent orchestration pipeline designed to automate the auditing of FAA/ICAO flight plan equipment codes against live aircraft maintenance registries.

🏗️ System Architecture
This crew utilizes a sequential orchestration pattern to identify, audit, and remediate flight dispatch equipment code mismatches.
 `![Architecture Diagram](assets/AviationWorkflow.png)`

The Multi-Agent Workflow
Flight Safety Data Analyst: Scans the telemetry queue to extract flights marked as PENDING.

Hangar Inventory Manager: Executes secure tool calls to cross-reference flight data against the live MRO registry.

Line Mechanic Foreman: Synthesizes findings, flags regulatory non-compliance, and drafts a formal dispatch correction notice requiring human authorization.

🛠️ Tech Stack
Framework: CrewAI (Hierarchical & Sequential Task Orchestration)

LLM Engine: OpenAI gpt-4o-mini

Tooling: Custom Python classes for secure file and registry interaction.

Governance: Human-in-the-Loop (HITL) safety gating.

📂 Component Structure
This crew is architected as a modular component of the global Airline-Operational-AI-Hub.

Plaintext
crews/tech_ops/
├── agents.py                 # Agent definitions, personas & LLM binding
├── tasks.py                  # Sequential task logic & callback definitions
└── tools.py                  # Custom Tool classes (MROInventoryTool)

🚀 Quick Start
Note: This crew is intended to be triggered by the root-level orchestrator.

Ensure environment variables are set in the project root .env file.

Execute from root:

python main_orchestrator.py

3. **Verify results:**
   The process will generate a formal compliance report located at `output/dispatch_compliance_alert.md`.

---

## ☁️ Production Roadmap
*   **Database Integration:** Replace local `mro_inventory.json` with **Google Cloud Firestore**.
*   **Telemetry Stream:** Replace local `mock_telemetry.csv` with **Google Cloud Pub/Sub** real-time ingestion.
*   **Audit Logging:** Stream all agent reasoning logs into **BigQuery** for FAA/ICAO regulatory reporting.

*Part of the Airline Operational AI Hub — Built to demonstrate scalable AI engineering practices for modern aviation operations.*