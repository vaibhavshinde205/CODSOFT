import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    return best_move

def get_valid_input():
    while True:
        user_input = input("Your turn (1-9): ")

        if user_input.strip() == "":
            print("Error: Input cannot be blank!")
            continue

        if not user_input.isdigit():
            print("Error: Please enter a valid number between 1 and 9!")
            continue

        move = int(user_input) - 1

        if move < 0 or move > 8:
            print("Error: Number must be between 1 and 9!")
            continue

        if board[move] != " ":
            print("Error: Position already taken!")
            continue

        return move


print("TIC TAC TOE - Human (X) vs Unbeatable AI (O)")
print_board()

current_player = "X"

while True:

    if current_player == "X":
        move = get_valid_input()
    else:
        print("Computer is thinking...")
        move = computer_move()

    board[move] = current_player

    print_board()

    if check_winner(current_player):
        if current_player == "X":
            print("Congratulations! You somehow won!")
        else:
            print("Computer wins!")
        break

    if is_draw():
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
