from dataclasses import dataclass

import chess


@dataclass
class ChessBoard:
    move: str | None = None
    board_state: str = (
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )


def _load_board(board_state: str) -> chess.Board:
    try:
        return chess.Board(board_state)
    except Exception as exc:
        raise ValueError(f'The board state is invalid: {board_state}') from exc


def count_legal_moves(chess_board: ChessBoard) -> int:
    board = _load_board(chess_board.board_state)

    if chess_board.move:
        board_move = chess.Move.from_uci(chess_board.move)
        if not board.is_legal(board_move):
            raise ValueError(f'{board_move} is illegal!')
        board.push(board_move)

    return board.legal_moves.count()


def generate_legal_moves(chess_board: ChessBoard) -> list[str]:
    move_list = []
    board = _load_board(chess_board.board_state)

    for move in board.legal_moves:
        move_list.append(move.uci())

    return sorted(move_list)


def encode_to_ascii(text: str) -> list[int]:
    encoded_text = [ord(letter) for letter in text]

    return encoded_text
