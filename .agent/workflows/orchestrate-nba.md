---
description: Coordinate multi-agent tasks for the NBA AI project.
---

# Workflow: NBA AI Orchestration

Use this workflow when tackling complex tasks like designing the GenAI engine or refactoring a core module.

## Protocol

1. **Phase 1: Discovery (Orchestrator)**
   - Analyze requirements against the North Star: "GenAI-based prediction engine from PBP data".
   - Identify affected modules (Etl, Predictions, WebApp).

2. **Phase 2: Planning (Project Planner)**
   - Create a detailed `{task-slug}.md`.
   - Break down implementation into sequential stages (matches the 9-stage pipeline if applicable).

3. **Phase 3: Execution (Specialists)**
   - **Backend Specialist**: ETL or API changes. Load `nba-ai-core` skill.
   - **Performance Optimizer**: GenAI model optimization or database query speedups.
   - **Frontend Specialist**: Dashboard improvements.

4. **Phase 4: Validation (Test Engineer / Security Auditor)**
   - Run `pytest`.
   - Run `python -m src.health_check`.
   - Run `.agent/scripts/checklist.py`.

5. **Phase 5: Release**
   - User approval.
   - Manual push to personal/public remote.
