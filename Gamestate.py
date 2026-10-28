"""Program made to determine the state of a tic-tac-toe."""

def has_won(board, player):
    """The rules to determine who wins in the game."""
    lines = []

    lines.extend(board)

    for col in range(3):
        lines.append("".join(row[col] for row in board))

    lines.append("".join(board[item][item] for item in range(3)))
    lines.append("".join(board[item][2 - item] for item in range(3)))

    return any(line == player * 3 for line in lines)


def gamestate(board):
    """The actual state of the game."""
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    x_wins = has_won(board, "X")
    o_wins = has_won(board, "O")

    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")

    if x_count - o_count > 1:
        raise ValueError("Wrong turn order: X went twice")

    if x_wins and o_wins:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_wins:
        if x_count != o_count + 1:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    if o_wins:
        if x_count != o_count:
            raise ValueError(
                "Impossible board: game should have ended after the game was won"
            )
        return "win"

    if all(cell != " " for row in board for cell in row):
        return "draw"

    return "ongoing"