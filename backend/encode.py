import chess


def generate_legal_moves() -> int:
    board = chess.Board()

    return board.legal_moves.count()
