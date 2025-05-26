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

├── data/                         # Contains all the PGN files for each grandmaster  
│   ├── Carlsen.pgn  
│   ├── Nakamura.pgn  
│   └── ... (other PGN files)  
├── chess_model_train.ipynb      # Main Colab notebook for training the model  
├── chess_master_model_pkl_file.zip  # Zipped trained model (.pkl)  
├── README.md                    # Project documentation  

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

### 🧪 Option 1: Run Locally

1. **Clone the repository**:
   
   -git clone https://github.com/Madhavan12103/-Chess-Game-Result-Prediction-Using-Machine-Learning.git
   -cd -Chess-Game-Result-Prediction-Using-Machine-Learning
2. **Install the required packages**:
   -pip install -r requirements.txt

3. **Run the Streamlit app**:
   -streamlit run main.py

4. **Use the app**:

   * Upload a `.pgn` (Portable Game Notation) file of a chess match.
   * The app will extract features and display the predicted result:

     * 🟢 **White Win**
     * ⚫ **Black Win**
     * ⚪ **Draw**

### 🌐 Option 2: Use the Web App

You can try the app directly on Streamlit Cloud without downloading anything:

🔗 [Click here to open the live app](https://pvyulhrityfrya6exqmrzp.streamlit.app/)

1. Open the link.
2. Upload your `.pgn` file.
3. View the predicted result instantly.

### 🧠 Option 3: Train the Model Yourself

If you'd like to retrain the model:

1. Open the Jupyter Notebook:
   -jupyter notebook chess_model_train.ipynb
   
2. Follow the steps inside the notebook to:

   * Load PGN files
   * Extract features
   * Train the model using Random Forest
   * Save the model as `chess_master_model.pkl`

3. Replace the existing `.pkl` file in your project directory if needed.

## 📥 How PGN Files Were Collected

-PGN files downloaded from Lichess/Chess.com or public databases.
-Parsed with chess.pgn in Python.
-ELO ratings and outcomes extracted from headers.
-Missing ELOs filled with default value (e.g., 1500).

## 📚 Future Work
- Add ECO opening code as a feature.
- Try XGBoost or SVM models for comparison.
- Train on larger dataset from all Lichess users.
- Include time control (Blitz, Bullet, Classical) as a feature.

## 🙋‍♂️ Author
Madhavan  
Aspiring Data Analyst | Machine Learning Enthusiast  
📧 madhavan12j@gmail.com  

