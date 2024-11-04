# nba_betting_model.py

from data_collection import get_game_data_for_seasons
from data_processing import process_game_data
from feature_engineering import add_recent_performance_features
from model import train_model
from evaluation import simulate_betting
import pandas as pd

# List of season(s) to fetch data for
seasons = ['2021-22']  # Type in desired seasons
season_type = 'Regular Season'

# Fetch game data for the specified seasons
game_data = get_game_data_for_seasons(seasons, season_type)
3
if game_data is not None:
    # Process data
    processed_data = process_game_data(game_data)
    
    # Add recent performance features
    enhanced_data = add_recent_performance_features(processed_data)
    
    # Train the model and evaluate its performance
    model, X_test, y_test, y_pred = train_model(enhanced_data)
    
    # Simulate betting with even odds of 2.0
    odds = pd.Series([2.0] * len(y_test))  # Assuming even odds for simplicity
    profit = simulate_betting(y_test, y_pred, odds)
    
    print(f"Total Profit from Betting Simulation: ${profit:.2f}")
