# ♟️ Chess Game Result Prediction Using Machine Learning

This project uses machine learning to predict the result of a chess game (Win for White, Win for Black, or Draw) using data from real games played by top grandmasters. The project showcases end-to-end skills in data extraction, feature engineering, model training, evaluation, and deployment.

## 📌 Project Overview

- **Objective**: Predict the outcome of a chess game based on ELO ratings and number of moves.
- **Dataset**: PGN files from top chess grandmasters including:
  - Magnus Carlsen
  - Hikaru Nakamura
  - Gukesh D
  - Arjun Erigaisi
  - Fabiano Caruana
  - Nodirbek Abdusattorov
  - Praggnanandhaa R
  - Viswanathan Anand

## 📁 Project Structure



## 📊 Features Used

| Feature         | Description                          |
|----------------|--------------------------------------|
| `white_elo`     | ELO rating of White player           |
| `black_elo`     | ELO rating of Black player           |
| `num_moves`     | Number of moves in the game          |
| `result`        | Target label (White, Black, Draw)    |

Additional features can be added such as opening codes, piece captures, or time control for improved accuracy.

## 🧠 Model

- **Algorithm**: Random Forest Classifier
- **Parameters**: `n_estimators=100`, `random_state=42`
- **Evaluation Metric**: Precision, Recall, F1-score, Accuracy

### 📈 Final Results:

Based on ~7000 games from 8 top GMs:

| Class  | Precision | Recall | F1-score |
|--------|-----------|--------|----------|
| Black  | 0.60      | 0.57   | 0.58     |
| Draw   | 0.53      | 0.50   | 0.51     |
| White  | 0.64      | 0.69   | 0.66     |
| **Accuracy** |      |        | **0.59** |

## 🔍 Observations

- **Draws** are the hardest to predict due to overlap in features.
- **White wins** are more frequent with higher precision.
- Adding openings and more features could improve performance.

## 🛠️ Installation

git clone https://github.com/yourusername/chess-result-prediction.git
cd chess-result-prediction
pip install -r requirements.txt

## ▶️ Usage
- Run the notebook
- jupyter notebook chess_model_train.ipynb
- Then upload your .pgn file and get the predicted result.

## 📥 How PGN Files Were Collected
- Downloaded .pgn files from Lichess/Chess.com/official databases for each GM.
- Cleaned using chess.pgn parser in Python.
- ELOs and results were extracted from headers.
- Missing ELOs filled with a fallback default (e.g., 1500).

## 📚 Future Work
- Add ECO opening code as a feature.
- Try XGBoost or SVM models for comparison.
- Train on larger dataset from all Lichess users.
- Include time control (Blitz, Bullet, Classical) as a feature.

## 🙋‍♂️ Author
Madhavan 
Aspiring Data Analyst | Machine Learning Enthusiast  
📧 madhavan12j@gmail.com  

