from backend.encode import generate_legal_moves


def test_generate_all_legal_moves_from_starting_position():
    legal_moves_from_start = generate_legal_moves()

    assert legal_moves_from_start == 20


def test_generate_all_legal_moves_from_any_position():
    legal_move_from_any_position = generate_legal_moves(
        '3bkb2/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1', 'e2e4'
    )

    assert legal_move_from_any_position == 18
