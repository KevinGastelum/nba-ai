---
description: Run the comprehensive system health check script for database validation.
---

# Workflow: Run NBA AI Health Check

This workflow validates the integrity of the seasonal database.

## Steps

1. **Verify Environment**
   Ensure `venv` is activated.

2. **Run Health Check CLI**
   Run the following command, replacing `<season>` (e.g., 2025-2026).

// turbo
```bash
python -m src.health_check --season=<season> --skip-pipeline
```

3. **Analyze Results**
   - **Exit Code 0**: Everything looks good.
   - **Exit Code 1**: Warning - some data may be missing or inconsistent.
   - **Exit Code 2**: Critical Failure - database structural issues found.

4. **Address Failures**
   If critical failures are found, investigate the specific table or flag mentioned in the output.
