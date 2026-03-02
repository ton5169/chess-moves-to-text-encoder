import chess

FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'


def main():
    move_list = []
    board = chess.Board(FEN)
    move = chess.Move.from_uci('e2e4')
    for move in board.legal_moves:
        move_list.append(move.uci())

    print(sorted(move_list))


if __name__ == '__main__':
    main()
