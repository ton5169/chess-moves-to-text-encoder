import math

import chess
from encode import ChessBoard


def digits_per_char(base):
    return math.ceil(math.log(128) / math.log(base))


def ascii_from_base_n(digits, base):
    n = digits_per_char(base)
    chars = []
    for i in range(0, len(digits), n):
        chunk = digits[i : i + n]
        value = 0
        for d in chunk:
            value = value * base + d
        chars.append(chr(value))
    return ''.join(chars)


def decode(moves: list[str], chess_board: ChessBoard, N: int):
    digits = []
    for move_uci in moves:
        legal = sorted([m.uci() for m in chess_board.board.legal_moves])
        digits.append(legal.index(move_uci))
        chess_board.board.push(chess.Move.from_uci(move_uci))
    return ascii_from_base_n(digits, N)
