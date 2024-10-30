# data_processing.py

import pandas as pd

def process_game_data(data):
    """
    Clean and preprocess NBA game data for modeling.

    Parameters:
    data (pd.DataFrame): Raw NBA game data.

    Returns:
    pd.DataFrame: Processed game data ready for analysis.
    """
    # Drop rows with missing values
    data = data.dropna()
    
    # Filter relevant columns, including GAME_DATE
    relevant_columns = ['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'PTS', 'WL', 'GAME_DATE']
    data = data[relevant_columns]
    
    # Encode 'WL' column (Win/Loss) as 1 for Win and 0 for Loss
    data['WL'] = data['WL'].apply(lambda x: 1 if x == 'W' else 0)
    
    # Convert team names to numerical codes if necessary
    data['TEAM_NAME'] = data['TEAM_NAME'].astype('category').cat.codes
    
    print("Data processing complete.")
    return data

