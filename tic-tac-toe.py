# Import tkinter library - this is used to create graphical user interfaces (windows, buttons, etc.)
import tkinter as tk
from tkinter import messagebox

# This is our main game class - think of it as a container that holds everything about our game
class TicTacToe:
    def __init__(self):
        # Create the main window for our game
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe Game")  # Set window title
        
        # Game state variables
        self.current_player = "X"  # X always starts first
        self.board = [""] * 9  # Create a list with 9 empty strings (one for each square)
        self.buttons = []  # This will store all our button widgets
        
        # Create the game interface
        self.create_widgets()
    
    def create_widgets(self):
        """This function creates all the visual elements (buttons, labels, etc.)"""
        
        # Create a label to show whose turn it is
        self.label = tk.Label(
            self.window, 
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 16, "bold"),
            pady=10
        )
        self.label.pack()  # pack() adds the label to the window
        
        # Create a frame (container) for our game board
        board_frame = tk.Frame(self.window)
        board_frame.pack(pady=10)
        
        # Create 9 buttons in a 3x3 grid
        # row goes from 0 to 2 (3 rows)
        for row in range(3):
            # col goes from 0 to 2 (3 columns)
            for col in range(3):
                # Calculate button index (0-8)
                # For example: row=0, col=0 gives index 0
                #              row=1, col=2 gives index 5
                index = row * 3 + col
                
                # Create a button
                button = tk.Button(
                    board_frame,
                    text="",  # Start with empty text
                    font=("Arial", 24, "bold"),
                    width=5,
                    height=2,
                    # When clicked, call button_click with this button's index
                    command=lambda i=index: self.button_click(i)
                )
                
                # Place button in grid at specific row and column
                button.grid(row=row, column=col, padx=5, pady=5)
                
                # Add button to our list so we can access it later
                self.buttons.append(button)
        
        # Create a "New Game" button
        new_game_button = tk.Button(
            self.window,
            text="New Game",
            font=("Arial", 12),
            command=self.reset_game  # Call reset_game when clicked
        )
        new_game_button.pack(pady=10)
    
    def button_click(self, index):
        """This function runs when a player clicks a button"""
        
        # Check if the square is already taken
        # If board[index] is not empty, it means someone already played there
        if self.board[index] != "":
            messagebox.showwarning("Invalid Move", "That square is already taken!")
            return  # Exit the function early
        
        # Update the game board data
        self.board[index] = self.current_player
        
        # Update the button's text to show X or O
        self.buttons[index].config(text=self.current_player)
        
        # Check if current player won
        if self.check_winner():
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins! 🎉")
            self.disable_all_buttons()  # Stop players from clicking more buttons
            return
        
        # Check if the game is a tie (all squares filled, no winner)
        if "" not in self.board:
            messagebox.showinfo("Game Over", "It's a tie! 🤝")
            return
        
        # Switch to the other player
        # If current player is X, switch to O. If O, switch to X.
        self.current_player = "O" if self.current_player == "X" else "X"
        
        # Update the label to show whose turn it is now
        self.label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self):
        """This function checks if someone won the game"""
        
        # All possible winning combinations (indices on the board)
        winning_combinations = [
            [0, 1, 2],  # Top row
            [3, 4, 5],  # Middle row
            [6, 7, 8],  # Bottom row
            [0, 3, 6],  # Left column
            [1, 4, 7],  # Middle column
            [2, 5, 8],  # Right column
            [0, 4, 8],  # Diagonal (top-left to bottom-right)
            [2, 4, 6]   # Diagonal (top-right to bottom-left)
        ]
        
        # Check each winning combination
        for combo in winning_combinations:
            # Get the values at the three positions
            a, b, c = combo
            
            # Check if all three positions have the same player (X or O)
            # and are not empty
            if (self.board[a] == self.board[b] == self.board[c] 
                and self.board[a] != ""):
                # Highlight the winning buttons
                for i in combo:
                    self.buttons[i].config(bg="lightgreen")
                return True  # Someone won!
        
        return False  # No winner yet
    
    def disable_all_buttons(self):
        """This function disables all buttons so no more moves can be made"""
        for button in self.buttons:
            button.config(state="disabled")  # Disable the button
    
    def reset_game(self):
        """This function resets everything for a new game"""
        
        # Reset game state
        self.current_player = "X"
        self.board = [""] * 9  # Clear the board
        
        # Reset all buttons
        for button in self.buttons:
            button.config(
                text="",  # Clear text
                state="normal",  # Enable button
                bg="SystemButtonFace"  # Reset background color to default
            )
        
        # Update label
        self.label.config(text=f"Player {self.current_player}'s Turn")
    
    def run(self):
        """This function starts the game"""
        self.window.mainloop()  # Keep the window open and responsive


# This is the starting point of our program
# Create a new game and run it
if __name__ == "__main__":
    game = TicTacToe()
    game.run()