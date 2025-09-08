import math

board = [' '] * 9

def print_board():
    cells = [board[i] if board[i] != ' ' else str(i+1) for i in range(9)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()

def check_winner():
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

def ai_move():
    empties = [i for i,v in enumerate(board) if v == ' ']
    if 4 in empties:
        return 4
    idx = math.floor(math.fmod(len(empties) * math.pi, len(empties)))
    return empties[idx]

def user_move():
    while True:
        try:
            pos = int(input("Your move (1-9): ").strip()) - 1
            if pos not in range(9):
                print("Choose 1-9.")
            elif board[pos] != ' ':
                print("Taken.")
            else:
                return pos
        except ValueError:
            print("Enter number 1-9.")

def main():
    print("You are X, AI is O.")
    print_board()
    while True:
        pos = user_move()
        board[pos] = 'X'
        print_board()
        result = check_winner()
        if result:
            break
        move = ai_move()
        board[move] = 'O'
        print(f"AI chose {move+1}")
        print_board()
        result = check_winner()
        if result:
            break
    if result == 'Tie':
        print("Tie!")
    else:
        print(f"{result} wins!")

if __name__ == "__main__":
    main()