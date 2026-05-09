#!/usr/bin/python3

def print_board(board):
    """
    Description:
        Displays the Tic-Tac-Toe board.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        None
    """

    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    """
    Description:
        Checks whether a player has won the game.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        str or None:
            Returns "X" or "O" if there is a winner.
            Returns None if there is no winner.
    """

    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        if (
            board[0][col] ==
            board[1][col] ==
            board[2][col] and
            board[0][col] != " "
        ):
            return board[0][col]

    # Check diagonal
    if (
        board[0][0] ==
        board[1][1] ==
        board[2][2] and
        board[0][0] != " "
    ):
        return board[0][0]

    # Check opposite diagonal
    if (
        board[0][2] ==
        board[1][1] ==
        board[2][0] and
        board[0][2] != " "
    ):
        return board[0][2]

    return None


def board_full(board):
    """
    Description:
        Checks whether the board is completely full.

    Parameters:
        board (list): 2D list representing the game board.

    Returns:
        bool:
            True if the board is full.
            False otherwise.
    """

    for row in board:
        if " " in row:
            return False

    return True


def get_valid_input(player):
    """
    Description:
        Safely gets and validates row and column input
        from the user.

    Parameters:
        player (str): Current player symbol ("X" or "O").

    Returns:
        tuple:
            Valid row and column coordinates.
    """

    while True:

        try:
            row = int(
                input(
                    f"Enter row (0, 1, or 2) "
                    f"for player {player}: "
                )
            )

            col = int(
                input(
                    f"Enter column (0, 1, or 2) "
                    f"for player {player}: "
                )
            )

            # Check valid range
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Row and column must be 0, 1, or 2.")
                continue

            return row, col

        except ValueError:
            print("Invalid input. Please enter numbers only.")


def tic_tac_toe():
    """
    Description:
        Runs the Tic-Tac-Toe game loop.

    Parameters:
        None

    Returns:
        None
    """

    board = [[" "] * 3 for _ in range(3)]

    player = "X"

    while True:

        print_board(board)

        row, col = get_valid_input(player)

        # Check if spot is taken
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place move
        board[row][col] = player

        # Check winner
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # Check tie
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        if player == "X":
            player = "O"
        else:
            player = "X"


tic_tac_toe()
