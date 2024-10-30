import pandas as pd
#Split arrays or matrices into random train and test subsets
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

"""
Train a logistic regression model to predict game outcomes.

Parameters:
data (pd.DataFrame): Processed NBA game data with features.

Returns:
model: Trained logistic regression model.
X_test (pd.DataFrame): Test features for evaluation.
y_test (pd.Series): True labels for test set.
y_pred (pd.Series): Predictions for test set.

"""
def train_model(data):
    X = data[['Recent_Avg_PTS', 'Recent_Win_Percent']]
    y=data['WL']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate model performance
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    return model, X_test, y_test, y_pred

