import pytest

from backend.encode import (
    ChessBoard,
    count_legal_moves,
    encode_to_ascii,
    encoding_ascii_to_moves,
    generate_legal_moves,
)


@pytest.fixture
def chess_board_start_position():
    return ChessBoard(
        board_state='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
    )


@pytest.fixture
def chess_board_illegal_move():
    return ChessBoard(
        board_state='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        move='e2e1',
    )


class TestChessBoardCounts:
    @pytest.mark.parametrize(
        'board_state, move, expected_result',
        [
            (
                'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
                None,
                20,
            ),
            ('3bkb2/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1', 'e2e4', 16),
        ],
        ids=[
            'starting-position - no move',
            'custom-position - e2e4',
        ],
    )
    def test_count_legal_moves(
        self, board_state: str, move: str, expected_result: int
    ) -> None:
        board = ChessBoard(move, board_state)
        legal_moves_from_start = count_legal_moves(board)

        assert legal_moves_from_start == expected_result


class TestChessBoardMoves:
    def test_generate_legal_moves(self, chess_board_start_position) -> None:
        legal_moves = generate_legal_moves(chess_board_start_position)

        assert legal_moves == [
            'a2a3',
            'a2a4',
            'b1a3',
            'b1c3',
            'b2b3',
            'b2b4',
            'c2c3',
            'c2c4',
            'd2d3',
            'd2d4',
            'e2e3',
            'e2e4',
            'f2f3',
            'f2f4',
            'g1f3',
            'g1h3',
            'g2g3',
            'g2g4',
            'h2h3',
            'h2h4',
        ]

    def test_raise_value_error_for_illegal_move(
        self, chess_board_illegal_move
    ) -> None:
        with pytest.raises(ValueError) as excinfo:
            count_legal_moves(chess_board_illegal_move)

        assert 'is illegal' in str(excinfo.value)

    def test_raise_value_error_for_invalid_board(self) -> None:
        with pytest.raises(ValueError) as excinfo:
            ChessBoard(
                board_state='rnbqkbnrr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
            )

        assert 'The board state is invalid' in str(excinfo.value)


class TestChessEncode:
    def test_encoding_from_letter_to_ascii(self) -> None:
        letter = 'h'
        encoded_text = encode_to_ascii(letter)
        assert encoded_text == [104]

    def test_encoding_ascii_to_moves(self, chess_board_start_position) -> None:
        encoded_text = [104, 105]
        encoded_moves = encoding_ascii_to_moves(
            encoded_text, chess_board_start_position, 16
        )

        assert encoded_moves == ['c2c3', 'd7d5', 'd1a4', 'c7c6']
