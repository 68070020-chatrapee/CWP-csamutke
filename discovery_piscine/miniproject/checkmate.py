PIECES = "KPBRQ"


def parse_board(board):

    if not isinstance(board, str) or board == "":
        return None
    if board.endswith("\n"):
        board = board[:-1]
    rows = board.split("\n")
    size = len(rows)
    for row in rows:
        if len(row) != size:
            return None
    king_count = 0
    for row in rows:
        king_count += row.count("K")
    if king_count != 1:
        return None
    return rows


def find_king(rows):
    for r in range(len(rows)):
        for c in range(len(rows)):
            if rows[r][c] == "K":
                return r, c
    return None


def first_piece(rows, r, c, dr, dc):
    size = len(rows)
    r += dr
    c += dc
    while 0 <= r < size and 0 <= c < size:
        if rows[r][c] in PIECES:
            return rows[r][c]
        r += dr
        c += dc
    return None


def is_in_check(rows):
    size = len(rows)
    kr, kc = find_king(rows)


    for dc in (-1, 1):
        pr = kr + 1
        pc = kc + dc
        if 0 <= pr < size and 0 <= pc < size and rows[pr][pc] == "P":
            return True

    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if first_piece(rows, kr, kc, dr, dc) in ("R", "Q"):
            return True

    for dr, dc in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
        if first_piece(rows, kr, kc, dr, dc) in ("B", "Q"):
            return True

    return False


def checkmate(board):
    rows = parse_board(board)
    if rows is None:
        print("Error")
        return
    if is_in_check(rows):
        print("Success")
    else:
        print("Fail")
