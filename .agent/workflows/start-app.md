---
description: Start the Flask web application with specific parameters.
---

# Workflow: Start NBA AI Web App

This workflow launches the prediction dashboard.

## Steps

1. **Verify Environment**
   Ensure `venv` is activated.

2. **Select Parameters**
   - **Predictor**: `Baseline`, `Linear`, `Tree` (default), `MLP`, `Ensemble`.
   - **Log Level**: `INFO` (default), `DEBUG`.

3. **Launch Application**
// turbo
```bash
python start_app.py --predictor=<predictor> --log_level=<log_level>
```

4. **Access UI**
   Open `http://localhost:5000` in your browser.
