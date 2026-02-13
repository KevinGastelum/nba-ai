# NBA AI Development Guide

Welcome to the **NBA AI** project. This guide provides the operational standards for upgrading and building this system.

## 🚀 Mission
**Build a GenAI-based prediction engine from Play-by-Play (PBP) data.**

## 📂 System Map

- `src/database_updater/`: The ETL engine.
- `src/predictions/`: Where models and features live.
- `src/web_app/`: The Flask dashboard.
- `data/`: SQLite databases (use `dev` for daily work).

## 🛠️ Workflows

Use these slash commands to accelerate development:

- `/update-data`: Trigger the 9-stage ETL pipeline.
- `/health-check`: Validate database integrity.
- `/start-app`: Launch the prediction dashboard.
- `/orchestrate-nba`: Coordinate complex multi-agent tasks.

## 📜 Development Rules

### 1. Environment First
Always activate the virtual environment:
```powershell
.\venv\Scripts\activate
```

### 2. Timezones
- **Database**: Store as UTC.
- **Queries**: Use Eastern Time (ET).
- **Display**: Use the user's local timezone.

### 3. Data Sensitivity
- Treat `NBA_AI_full.sqlite` (25GB) with care; avoid large scans.
- Use CTEs and indexes for efficient queries.

### 4. No Transitive Dependencies
Keep `requirements.txt` clean. Only list direct dependencies.

### 5. Ask Before Committing
Always verify with the user before performing a Git commit.

## 🧠 Predicition Pipeline
To add a new model:
1. Inherit from `BasePredictor` in `src/predictions/prediction_engines/`.
2. Implement `make_pre_game_predictions` and `make_current_predictions`.
3. Register the model in `prediction_manager.py`.
4. Update `config.yaml`.

## 📈 Sprint 17: GenAI Design
- Focus: Transformer models + PBP sequence data.
- Goal: Move away from manual feature engineering (the "34 features" pattern).
