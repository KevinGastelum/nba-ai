import logging
import json
from src.games_api.games import get_games_for_date
from src.web_app.game_data_processor import process_game_data
from src.logging_config import setup_logging

setup_logging(log_level="DEBUG")

import argparse

def test_fetch_and_process():
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", type=str, default="2026-02-12")
    parser.add_argument("--predictor", type=str, default="Tree")
    args = parser.parse_args()
    
    date = args.date
    predictor = args.predictor

    print(f"Fetching and processing games for {date} with {predictor}...")
    try:
        games = get_games_for_date(date, predictor=predictor, update_predictions=True)
        print(f"Found {len(games)} games.")
        
        # Test the processing layer
        processed = process_game_data(games)
        print(f"Processed {len(processed)} games.")
        
        for p_game in processed[:3]:
            print(f"\nGame: {p_game['home_full_name']} vs {p_game['away_full_name']}")
            print(f"  Status: {p_game['game_status']}")
            print(f"  Datetime Display: {p_game['datetime_display']}")
            print(f"  Pred Winner: {p_game['pred_winner']} ({p_game['pred_win_pct']})")
            print(f"  Logo URLs: {p_game['home_logo_url']}, {p_game['away_logo_url']}")
            print(f"  Num Home Players: {len(p_game['home_players'])}")

    except Exception as e:
        print(f"Error: {e}")
        logging.exception("Failed")

if __name__ == "__main__":
    test_fetch_and_process()
