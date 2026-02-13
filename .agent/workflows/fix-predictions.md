---
description: Troubleshooting and fixing missing or incorrect predictions
---

# Workflow: Fix Predictions

Use this workflow when a user reports missing predictions or if the web app shows "No Prediction" for a game.

## Phase 1: Diagnosis
1. Check completion flags for the game(s):
   ```bash
   python -m src.health_check --game_ids=id1,id2 --skip-pipeline
   ```
2. Verify if features exist in the `Features` table:
   ```sql
   SELECT COUNT(*) FROM Features WHERE game_id = 'your_game_id';
   ```

## Phase 2: Recovery
1. If features are missing, run the ETL up to stage 8:
   // turbo
   ```bash
   python -m src.database_updater.database_update_manager --game_ids=your_game_id --stage=8
   ```
2. Force prediction generation for a specific predictor:
   // turbo
   ```bash
   python -m src.database_updater.database_update_manager --game_ids=your_game_id --stage=9 --predictor=Tree
   ```

## Phase 3: Validation
1. Query the `Predictions` table to confirm JSON blob presence:
   ```sql
   SELECT prediction_set FROM Predictions WHERE game_id = 'your_game_id' AND predictor = 'Tree';
   ```
2. Refresh the web app or hit the API directly:
   ```bash
   curl "http://127.0.0.1:5000/api/games?game_id=your_game_id&predictor=Tree"
   ```

## Critical Notes
- **Pre-game Data Finalized**: Predictions REQUIRE `pre_game_data_finalized=1`.
- **Prior Games**: Team features require at least 1-2 prior games in the current season to be "complete".
- **Predictor Names**: Case sensitive. Always use 'Tree', 'Baseline', 'Linear', 'MLP', or 'Ensemble'.
