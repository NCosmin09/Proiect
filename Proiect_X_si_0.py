def display_board(board):
    for i in range(1, 10, 3):
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')
        if i < 7:
            print('---+---+---')

def check_winner(board, marker):
    return (
        any(all(board[i] == marker for i in line) for line in [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Orizontala
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Verticala
            [1, 5, 9], [3, 5, 7]              # Diagonala
        ])
    )

def is_board_full(board):
    return ' ' not in board[1:]

def get_player_move(board):
    position = 0
    while position not in range(1, 10) or board[position] != ' ':
        try:
            position = int(input("Introdu o valoare intre 1 si 9: "))
        except ValueError:
            print("Valoare invalida. Introdu un numar intre 1 si 9 .")
    return position

def tic_tac_toe_game():
    print("Sa inceapa jocul!")
    board = [' '] * 10
    players = ('X', 'O')
    current_player = 0

    while True:
        display_board(board)
        position = get_player_move(board)
        board[position] = players[current_player]

        if check_winner(board, players[current_player]):
            display_board(board)
            print(f"Jucatorul {players[current_player]} a castigat!")
            break
        elif is_board_full(board):
            display_board(board)
            print("Egalitate!")
            break

        current_player = (current_player + 1) % 2

if __name__ == '__main__':
    tic_tac_toe_game()
