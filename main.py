import streamlit as st
import chess.pgn
import chess.svg
from io import StringIO
import streamlit.components.v1 as components

st.title("♟️ Chess Game Result Predictor with Board Visualization")

st.markdown("Upload a PGN file and view the game on a chessboard. You can use the slider to step through the moves.")

# Upload the PGN file
uploaded_file = st.file_uploader("Upload a PGN file", type=["pgn"])
if uploaded_file:
    # Read PGN
    pgn = StringIO(uploaded_file.getvalue().decode("utf-8"))
    game = chess.pgn.read_game(pgn)
    
    if game:
        board = game.board()
        moves = list(game.mainline_moves())

        st.subheader("Game Details")
        st.markdown(f"**White**: {game.headers.get('White', 'Unknown')}")
        st.markdown(f"**Black**: {game.headers.get('Black', 'Unknown')}")
        st.markdown(f"**Result**: {game.headers.get('Result', 'Unknown')}")

        # Slider to move through the game
        move_num = st.slider("Move number", 0, len(moves), 0)

        # Play moves
        for i in range(move_num):
            board.push(moves[i])

        # Render board as SVG
        board_svg = chess.svg.board(board=board, size=400)
        components.html(board_svg, height=450)

        st.success(f"Displayed move {move_num} of {len(moves)}")
    else:
        st.error("Could not parse the PGN file.")
