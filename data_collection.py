# data_collection.py

from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
import time

def get_game_data_for_seasons(seasons, season_type='Regular Season'):
    """
    Fetch NBA game data for a list of seasons.

    Parameters:
    seasons (list): List of seasons in format YYYY-YY
    season_type (str): Type of season data to retrieve ('Regular Season', 'Playoffs')

    Returns:
    pd.DataFrame: Combined DataFrame containing game data for all specified seasons.
    
    """
    # Initialize empty DataFrame to store all season data
    all_games = pd.DataFrame()

    for season in seasons:
        try:
            # Fetch game data for the specified season and season type
            gamefinder = leaguegamefinder.LeagueGameFinder(
                season_nullable=season,
                season_type_nullable=season_type
            )
            season_games = gamefinder.get_data_frames()[0]  # Get the DataFrame for this season

            # Append the season's data to the master DataFrame
            all_games = pd.concat([all_games, season_games], ignore_index=True)
            
            print(f"Data for season {season} {season_type} loaded successfully.")
            
            # Add a small delay to avoid rate limiting
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching data for season {season}: {e}")

    return all_games

