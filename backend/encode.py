from dataclasses import dataclass

import chess


@dataclass
class ChessBoard:
    move: str | None = None
    board_state: str | None = (
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )


def generate_legal_moves(chess_board: ChessBoard) -> int:

    try:
        board = chess.Board(chess_board.board_state)
    except Exception as exc:
        raise ValueError(
            f'The board state is invalid: {chess_board.board_state}'
        ) from exc

    if chess_board.move:
        board_move = chess.Move.from_uci(chess_board.move)
        if not board.is_legal(board_move):
            raise ValueError(f'{board_move} is illegal!')
        board.push(board_move)

    return board.legal_moves.count()
