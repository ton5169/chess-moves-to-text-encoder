import chess

FEN = '3bkb2/pppppppp/8/8/8/8/PPPPPPPP/4K3 w - - 0 1'


def main():

    board = chess.Board(FEN)
    print(board.legal_moves.count())
    print(bool(board.legal_moves))
    move = chess.Move.from_uci('e2e4')
    for move in board.legal_moves:
        print(move)
    print(board.legal_moves.count())


if __name__ == '__main__':
    main()
