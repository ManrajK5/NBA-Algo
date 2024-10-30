import pandas as pd

def add_recent_performance_features(data, games_window=5):
    """
    Add recent performance features for each team based on the last few games.

    Parameters:
    data (pd.DataFrame): Processed NBA game data.
    games_window (int): The number of recent games to consider for calculating averages.

    Returns:
    pd.DataFrame: DataFrame with new features.
    """
    # Sort by team and game date to calculate rolling averages
    data = data.sort_values(by=['TEAM_ID', 'GAME_ID'])
    
    # Calculate recent average points for each team over the last `games_window` games
    data['Recent_Avg_PTS'] = data.groupby('TEAM_ID')['PTS'].transform(
        lambda x: x.rolling(window=games_window, min_periods=1).mean()
    )
    
    # Calculate recent win percentage over the last `games_window` games
    data['Recent_Win_Percent'] = data.groupby('TEAM_ID')['WL'].transform(
        lambda x: x.rolling(window=games_window, min_periods=1).mean()
    )
    
    print("Feature engineering complete.")
    return data