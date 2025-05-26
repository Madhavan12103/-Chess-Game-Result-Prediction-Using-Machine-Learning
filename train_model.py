# train_model.py

import chess.pgn
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
import os
import io

# Extract features from PGN files
def extract_features(pgn_text):
    games = []
    pgn_io = io.StringIO(pgn_text)

    while True:
        game = chess.pgn.read_game(pgn_io)
        if game is None:
            break

        try:
            result = game.headers["Result"]
            white_elo = int(game.headers.get("WhiteElo", 1500))
            black_elo = int(game.headers.get("BlackElo", 1500))
            num_moves = len(list(game.mainline_moves()))

            if result == "1-0":
                label = "White"
            elif result == "0-1":
                label = "Black"
            elif result == "1/2-1/2":
                label = "Draw"
            else:
                continue

            games.append({
                "white_elo": white_elo,
                "black_elo": black_elo,
                "num_moves": num_moves,
                "result": label
            })
        except:
            continue

    return games

# Load PGN files from folder
def extract_features_from_folder(folder_path="pgn_files"):
    all_games = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pgn"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                pgn_text = f.read()
                all_games.extend(extract_features(pgn_text))
    return pd.DataFrame(all_games)

# Run model training
def train_and_save_model():
    df = extract_features_from_folder()
    df.dropna(inplace=True)

    X = df[["white_elo", "black_elo", "num_moves"]]
    y = df["result"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "chess_master_model.pkl")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_and_save_model()
