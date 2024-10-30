# evaluation.py

import pandas as pd

def simulate_betting(y_test, y_pred, odds, bet_amount=100):
    """
    Simulate a betting strategy based on model predictions.

    Parameters:
    y_test (pd.Series): True game outcomes (1 for win, 0 for loss).
    y_pred (pd.Series): Model predictions (1 for win, 0 for loss).
    odds (pd.Series): Betting odds for each game.
    bet_amount (float): The amount to bet on each game.

    Returns:
    float: Total profit from the betting simulation.
    """

    # Initialize profit tracker
    total_profit = 0

    for actual, predicted, odd in zip(y_test, y_pred, odds):
        if predicted == 1:  # If the model predicts a win
            if actual == 1:  # If the model was correct (win predicted and it won)
                # Calculate winnings: bet_amount * (odds - 1)
                total_profit += bet_amount * (odd - 1)
            else:
                # Subtract the bet amount for a loss
                total_profit -= bet_amount

    return total_profit
