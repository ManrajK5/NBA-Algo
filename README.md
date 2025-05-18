# 🏀 NBA Game Outcome Predictor

A full-stack machine learning web app that predicts the winner of an NBA game using team Elo ratings. Built with React, Flask, and XGBoost, and deployed on AWS EC2.

---

## 🔍 Overview

This project allows users to input Elo ratings for the home and away NBA teams and returns a prediction of the expected winner and win probability. The model is trained on historical NBA data using Elo-based performance metrics.

---

## 🧠 Features

- 💡 **XGBoost Model**: Predicts NBA game outcomes based on engineered Elo features  
- 🌐 **Flask API**: Serves predictions from the trained model via a RESTful interface  
- ⚛️ **React Frontend**: Clean, responsive UI for Elo input and results display  
- ☁️ **Cloud Hosted**: Deployed on AWS EC2, accessible via public IP  
- 🔁 **Proxy Integration**: Frontend-to-backend connection using React dev proxy  

---

## 🚀 Tech Stack

- **Frontend**: React, Tailwind CSS  
- **Backend**: Flask, Python, joblib, XGBoost  
- **Deployment**: AWS EC2 (Ubuntu), SSH, Gunicorn/Flask Dev Server  
- **Data**: Historical NBA Elo and game results

---

## 🔧 Coming Soon: Features & Upgrades

- 🎨 **UI Redesign**: Improved layout and styling for mobile and desktop responsiveness  
- 📊 **Advanced Stats**: Use recent win percentage, player injuries, and team momentum  
- 🧠 **Model Upgrade**: Incorporate class rebalancing and more features for better accuracy  
- 🔍 **Error Feedback**: Show more detailed errors and explanations for predictions  
- 📈 **Live Game Mode**: Track upcoming matchups and provide daily predictions  
- 🌐 **Full Deployment**: Serve React frontend publicly alongside Flask backend

### 📁 Backend
```bash
cd nba-predictor-backend
python3 -m venv nba-env
source nba-env/bin/activate
pip install -r requirements.txt
python api.py
