from dataclasses import dataclass, field

import chess


@dataclass
class ChessBoard:
    move: str | None = None
    board_state: str = (
        'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )
    board: chess.Board = field(default_factory=chess.Board)

    def __post_init__(self):
        try:
            self.board = chess.Board(self.board_state)
        except Exception as exc:
            raise ValueError(
                f'The board state is invalid: {self.board_state}'
            ) from exc


def to_base_n(ascii_values, base):
    digits = []
    for value in ascii_values:
        if value == 0:
            digits.append(0)
            continue
        number_digits = []
        while value > 0:
            number_digits.append(value % base)
            value //= base
        number_digits.reverse()
        digits.extend(number_digits)
    return digits


def count_legal_moves(chess_board: ChessBoard) -> int:
    if chess_board.move:
        board_move = chess.Move.from_uci(chess_board.move)
        if not chess_board.board.is_legal(board_move):
            raise ValueError(f'{board_move} is illegal!')
        chess_board.board.push(board_move)

    return chess_board.board.legal_moves.count()


def generate_legal_moves(chess_board: ChessBoard) -> list[str]:
    move_list = []

    for move in chess_board.board.legal_moves:
        move_list.append(move.uci())

    return sorted(move_list)


def encode_to_ascii(text: str) -> list[int]:
    encoded_text = [ord(letter) for letter in text]

    return encoded_text


def encoding_ascii_to_moves(
    encoded_text: list[int], chess_board: ChessBoard, N: int
) -> list[str]:
    move_list = []
    digits = to_base_n(encoded_text, N)

    for digit in digits:
        legal_moves = sorted([m.uci() for m in chess_board.board.legal_moves])
        chosen = legal_moves[digit % len(legal_moves)]
        chess_board.board.push(chess.Move.from_uci(chosen))
        move_list.append(chosen)

    return move_list
