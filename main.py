import streamlit as st
import chess.pgn
import chess.svg
import streamlit.components.v1 as components
import pandas as pd
import io
import joblib
import zipfile
import os

# 🔓 Unzip model if not already extracted
if not os.path.exists("chess_master_model.pkl"):
    with zipfile.ZipFile("chess_master_model_pkl_file.zip", 'r') as zip_ref:
        zip_ref.extractall()

# ✅ Load trained ML model
model = joblib.load("chess_master_model.pkl")

# 🎯 Streamlit App
st.set_page_config(page_title="Chess PGN Predictor", page_icon="♟️")
st.title("♟️ PGN Game Result Predictor")
st.markdown("Upload a PGN file and see what the ML model predicts.")

uploaded_file = st.file_uploader("Upload a PGN file", type=["pgn"])

if uploaded_file:
    # 🔍 Parse the PGN
    pgn_text = io.StringIO(uploaded_file.getvalue().decode("utf-8"))
    game = chess.pgn.read_game(pgn_text)

    if game is None:
        st.error("❌ Could not read game from PGN file.")
    else:
        board = game.board()
        moves = list(game.mainline_moves())

        # 📊 Extract metadata
        white_elo = int(game.headers.get("WhiteElo", 1500))
        black_elo = int(game.headers.get("BlackElo", 1500))
        num_moves = len(moves)

        # 🤖 Predict result
        input_df = pd.DataFrame([{
            "white_elo": white_elo,
            "black_elo": black_elo,
            "num_moves": num_moves
        }])

        prediction = model.predict(input_df)[0]
        st.success(f"✅ Predicted Result: **{prediction}**")

        st.markdown("### 📍 Visualize Game Moves")
        move_num = st.slider("Select Move Number", 0, len(moves), len(moves), help="This move count is also used in prediction.")
        preview_board = game.board()
        for move in moves[:move_num]:
            preview_board.push(move)

        svg_image = chess.svg.board(board=preview_board, size=400)
        components.html(svg_image, height=500)

        if move_num == len(moves):
            st.info("👆 The final board position used for prediction is shown above.")
        else:
            st.warning("⬆️ Move slider to the final position to view the state used for prediction.")

        st.markdown("### ℹ️ Game Info")
        st.write(f"**White Elo**: {white_elo}")
        st.write(f"**Black Elo**: {black_elo}")
        st.write(f"**Total Moves**: {num_moves}")
