board = [" " for _ in range(9)]

def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

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

def play():
    current = "X"
    for _ in range(9):
        print_board()
        move = int(input(f"Player {current}, enter position (0-8): "))
        
        if board[move] == " ":
            board[move] = current
            if check_winner(current):
                print_board()
                print(f"{current} wins!")
                return
            current = "O" if current == "X" else "X"
        else:
            print("Invalid move")

    print("It's a draw!")

play()
