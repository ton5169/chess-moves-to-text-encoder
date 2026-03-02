import pytest

from backend.decode import ascii_from_base_n, decode
from backend.encode import ChessBoard


@pytest.fixture
def chess_board_start_position():
    return ChessBoard(
        board_state='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )


class TestChessDecode:
    def test_decoding_base_n_to_ascii(self) -> None:
        digits = [6, 8]
        decoded_text = ascii_from_base_n(digits, 16)

        assert decoded_text == 'h'

    def test_decoding_moves_to_text(self, chess_board_start_position) -> None:
        moves = ['c2c3', 'd7d5', 'd1a4', 'c7c6']
        decoded_text = decode(moves, chess_board_start_position, 16)

        assert decoded_text == 'hc'
