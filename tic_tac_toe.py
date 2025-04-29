import tkinter as tk
from tkinter import messagebox

# Initial board setup
board = [" " for _ in range(9)]  # 3x3 board flattened

# Function to print the board (for debugging purposes)
def print_board():
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        print("-" * 5)

# Check for winner
def check_winner(brd, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[i] == player for i in combo) for combo in win_conditions)

# Check if board is full
def is_full(brd):
    return " " not in brd

# Minimax algorithm to calculate the best move for AI
def minimax(brd, is_maximizing):
    if check_winner(brd, "O"): return 1
    if check_winner(brd, "X"): return -1
    if is_full(brd): return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, False)
                brd[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, True)
                brd[i] = " "
                best_score = min(score, best_score)
        return best_score

# Function to make the AI choose the best move
def best_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")
    check_game_status()

# Function to handle player move
def player_move(idx):
    if board[idx] == " ":
        board[idx] = "X"
        buttons[idx].config(text="X", state="disabled")
        check_game_status()
        ai_turn()

# Function to check the game status (win/tie)
def check_game_status():
    if check_winner(board, "X"):
        messagebox.showinfo("Game Over", "You win!")
        reset_game()
    elif check_winner(board, "O"):
        messagebox.showinfo("Game Over", "AI wins!")
        reset_game()
    elif is_full(board):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset_game()

# Function to reset the game
def reset_game():
    global board
    board = [" " for _ in range(9)]  # Reset the board
    for button in buttons:
        button.config(text=" ", state="normal")

# Function to handle AI turn
def ai_turn():
    best_move()

#Funtion for new game
def new_game():
    global board
    board = [" " for _ in range(9)]  # Reset the board
    for button in buttons:
        button.config(text=" ", state="normal")

#Function to end game
def end_game():
    for button in buttons:
        button.config(state="disabled")
    new_game_button.config(state="normal")


# Create the GUI window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create a list of buttons for the 3x3 grid
buttons = []
for i in range(9):
    button = tk.Button(window, text=" ", width=10, height=3, command=lambda i=i: player_move(i))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

#Create a new game button
new_game_button = tk.Button(window, text="New Game", command=new_game, width=10, height=2)
new_game_button.grid(row=3, column=0, columnspan=3)
new_game_button.config(state="normal")
new_game_button.forget()

# Create an end game button
end_game_button = tk.Button(window, text="End Game", width=10, height=2, command=window.destroy)
end_game_button.grid(row=4, column=0, columnspan=3)
end_game_button.config(state="normal")
end_game_button.forget()

# Start the GUI event loop
window.mainloop()
