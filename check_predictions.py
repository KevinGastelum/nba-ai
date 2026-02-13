import sqlite3
import json
import os
import sys

# Get database path from environment or default
db_path = os.environ.get("DATABASE_PATH", "data/NBA_AI_current.sqlite")

def query_predictions(date_substring):
    print(f"Connecting to database: {db_path}")
    if not os.path.exists(db_path):
        print("Database not found!")
        return
        
    try:
        # Use Read-Only mode to avoid locks
        uri = f"file:{db_path}?mode=ro"
        conn = sqlite3.connect(uri, uri=True)
        cursor = conn.cursor()
        
        # 1. Get Game IDs for approximate date
        print(f"Fetching games for date matching '{date_substring}%'...")
        query_games = "SELECT game_id, date_time_utc, home_team, away_team FROM Games WHERE date_time_utc LIKE ?"
        cursor.execute(query_games, (f"%{date_substring}%",))
        games = cursor.fetchall()
        
        if not games:
            print("No games found for this date substring.")
            conn.close()
            return

        print(f"Found {len(games)} games.")
        
        results = []
        for g in games:
            game_id, dt_utc, home, away = g
            
            # 2. Get Predictions
            query_preds = "SELECT predictor, prediction_set FROM Predictions WHERE game_id = ?"
            cursor.execute(query_preds, (game_id,))
            pred_rows = cursor.fetchall()
            
            game_preds = {}
            for pr in pred_rows:
                predictor, p_set = pr
                try:
                    game_preds[predictor] = json.loads(p_set)
                except:
                    game_preds[predictor] = "Invalid JSON"
            
            results.append({
                "game_id": game_id,
                "date": dt_utc,
                "home": home,
                "away": away,
                "predictions_found": list(game_preds.keys()),
                "tree_prediction": game_preds.get("Tree")
            })
            
        print(json.dumps(results, indent=2))
        conn.close()
    except Exception as e:
        print(f"Error querying database: {e}")

if __name__ == "__main__":
    query_predictions("2026-02-11")
