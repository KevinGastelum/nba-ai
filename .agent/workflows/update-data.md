---
description: Trigger the 9-stage database update pipeline for a specific season.
---

# Workflow: Update NBA AI Database

This workflow orchestrates the sequential ETL pipeline to update the SQLite database with the latest NBA data.

## Steps

1. **Verify Environment**
   Ensure `venv` is activated. If not, activate it first.

2. **Run Update Manager**
   Run the following command, replacing `<season>` (e.g., 2025-2026) and `<predictor>` (e.g., Tree).

// turbo
```bash
python -m src.database_updater.database_update_manager --season=<season> --predictor=<predictor>
```

3. **Monitor Output**
   Watch for log messages. The process works in 100-game chunks.

4. **Run Health Check**
   It's recommended to run `/health-check` after the update finishes.
