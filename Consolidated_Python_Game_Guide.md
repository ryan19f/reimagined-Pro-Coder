Consolidated Python Game Guide
This document combines a teaching guide for a basic Hangman game with full code implementations of a Mad Libs game and a Tic-Tac-Toe game, all presented with detailed explanations.
1. Hangman Teaching Guide
🎯 Objective
By the end of this session, learners will understand:
Input/output operations in Python
Using loops and conditionals
Working with strings
Basic logic building (game mechanics)
Intro to modules (time)
📝 Section 1: Getting Started
🧩 1.1 Import Required Module
import time

time.sleep() is used to pause the program for a short duration.
Beginner Tip: Think of it as saying “Hold on a second!” to the computer.
🙋 Section 2: User Interaction
💬 2.1 Ask for the User's Name
name = input("What is your name? ")
print("Hello," + name, "Time to play hangman!")

input() captures user input.
print() displays output.
Pro Tip: Use f-strings for cleaner syntax: print(f"Hello, {name}...")
🕓 Section 3: Add Some Drama
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)

Adds dramatic pauses for better user experience.
🔐 Section 4: Set the Secret Word
word = "springdales"
guesses = ''
turns = 10

word is the secret word.
guesses stores letters guessed by the user.
turns is the number of chances.
🔁 Section 5: The Main Game Loop
while turns > 0:
 failed = 0

Loop runs while turns remain.
failed tracks missing characters.
🔤 5.2 Check Each Character
for char in word:
 if char in guesses:
 print(char, end=' ')
 else:
 print("\_", end=' ')
 failed += 1

Shows guessed letters or underscores.
🎉 5.3 Win Condition
if failed == 0:
 print("You won")
 break

If all characters are guessed, the player wins.


🔡 Section 6: Player’s Guess
guess = input("guess a character: ")
guesses += guess

Captures and stores player's guess.
❌ Section 7: Wrong Guess Handling
if guess not in word:
 turns -= 1
 print("Wrong")
 print("You have", turns, 'more guesses')

Decreases turns and notifies user on wrong guesses.
💀 Section 8: Loss Condition
if turns == 0:
 print("You Lose")

Notifies user if no turns are left.
🔧 Fixes & Improvements
Use print(char, end=' ') instead of Python 2 print format.
Add case-insensitive input handling with .lower().
Optionally randomize the word from a list.
💡 Bonus Tips & Challenge Tasks
Beginner: Change the word. Customize messages.
Intermediate: Add score. Validate input.
Advanced: Add difficulty levels. ASCII Hangman drawing.




2. Mad Libs Game
This is a simple Mad Libs game that prompts the user for various types of words (adjectives, nouns, verbs) and then inserts them into a pre-written story. It uses tkinter for a basic GUI to display the final story.
🎯 Objective
By the end of this section, learners will understand:
How to get multiple inputs from the user.
How to store user input in variables.
How to concatenate strings to form a new sentence or story.
Basic introduction to tkinter for creating a simple graphical user interface (GUI) with labels.
📝 Section 1: Setting up the GUI and Getting User Input
🧩 1.1 Importing Tkinter
from tkinter import *

from tkinter import * imports all classes and functions from the tkinter module, which is Python's standard GUI (Graphical User Interface) library.
💬 1.2 Capturing User Inputs
adjective1 = input("Tell me an adjective, and click enter. ")
noun1 = input("Tell me a noun (plural), and click enter. ")
adjective2 = input("Tell me an adjective, and click enter. ")
noun2 = input("Tell me another noun, and click enter. ")
verb = input("Tell me a verb, and click enter. ")

These lines use the input() function to prompt the user for specific types of words.
Each word entered by the user is stored in its respective variable (e.g., adjective1, noun1).
Beginner Tip: The input() function always captures text as a string.



📣 1.3 Game Title and Initial Print
title =('Welcome to Mad libs Lets start')
print (title)

A simple string title is created and then printed to the console to welcome the user. This appears in the console where the input() prompts are shown, not in the tkinter window.
🖼️ 1.4 Initializing the Tkinter Window
master = Tk()
master.title('Mad Libs')
master.minsize(width=400, height=400)

master = Tk() creates the main window of the GUI application. This is typically called the "root" window.
master.title('Mad Libs') sets the title that appears in the window's title bar.
master.minsize(width=400, height=400) sets the minimum size that the window can be resized to.
Pro Tip: GUI applications are often preferred for games like Mad Libs to offer a more interactive and visually appealing experience than a pure console application.
📜 Section 2: Building and Displaying the Story
🔗 2.1 Assigning Variables for Clarity
x = adjective1
y = noun1
z = adjective2
a = noun2
b = verb

These lines re-assign the input variables to shorter, single-letter variables (x, y, z, a, b) for easier use within the long string concatenation. This is a stylistic choice and not strictly necessary for functionality.




📝 2.2 Creating the Story Label
w = Label(master, text="There was once a "+ x +" boy from Dubai"'\n'"who was baked by "+ y + " in a pie"'\n'" to his "+ z + "'s " + a+ " disgust "'\n'"he "+ b+" through the crust"'\n'"and exclaimed ,'what a good boy am I !'"'\n'"so are you happy with your wacky story!" )

Label(master, text=...) creates a text label widget. The master argument specifies that this label belongs to our main window.
The text argument contains the entire Mad Libs story, built by concatenating static strings with the user-provided variables (x, y, z, a, b).
'\n' is used to create new lines within the label's text, ensuring the story is displayed across multiple lines for readability.
Intermediate Tip: For longer strings or more complex formatting, consider using f-strings (e.g., f"There was once a {x} boy...") as they are generally cleaner and more efficient than repeated string concatenation.
📦 2.3 Packing the Label
w.pack()

w.pack() is a geometry manager that organizes widgets in blocks before placing them in the parent widget. It's a simple way to make the label visible in the window and take up enough space.
🔄 2.4 Running the Tkinter Event Loop
mainloop()

mainloop() is essential for any tkinter application. It starts the event loop, which listens for events (like button clicks, window resizing, etc.) and keeps the window open until it's closed by the user. Without this, the window would flash and disappear immediately.
💡 Bonus Tips & Challenge Tasks
Beginner: Change the story. Add more input fields for more complex sentences.
Intermediate: Use f-strings for the story text. Add a "Reset" button to play again without restarting the script.
Advanced: Create separate Frame widgets to organize the inputs and the story output. Add input validation (e.g., ensure an adjective is entered when asked for).

3. Tic-Tac-Toe Game
This is a command-line Tic-Tac-Toe game where the player plays against a simple AI.
🎯 Objective
By the end of this section, learners will understand:
How to represent a game board using a Python list.
Implementing game logic for moves, win conditions, and draws.
Using random module for computer's starting turn.
Developing a basic AI strategy (win immediately, block opponent, then prioritize specific moves).
Handling basic user input and invalid moves.
📝 Section 1: Game Setup and Board Representation
🧩 1.1 Importing Modules
import random
import sys # Though sys is imported, it's not explicitly used in the provided code snippet.

import random: This module is used to randomly select which player (human or computer) goes first and to decide which character ('X' or 'O') they will use.
import sys: While imported, sys functions are not explicitly called in the provided code. It is often used for system-specific parameters and functions, like sys.exit() to terminate the program.
📏 1.2 Initializing Game Variables
board=[i for i in range(0,9)]
player, computer = '',''

# Predefined moves for computer to prioritize
moves=((1,7,3,9),(5,),(2,4,6,8))
# Winning combinations (indices of the board list)
winners=((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
tab=range(1,10) # Valid board positions (1-9 for user input)

board=[i for i in range(0,9)]: This creates the game board as a list. Initially, it contains numbers 0 through 8, representing the available positions. As moves are made, these numbers will be replaced by 'X' or 'O'.
player, computer = '','': These variables will store the characters assigned to the human player and the computer.
moves: This tuple of tuples defines a strategic order for the computer's moves: corners (1,7,3,9), then center (5), then edges (2,4,6,8). This helps the AI play more strategically.
winners: This tuple of tuples contains all possible winning combinations on the board (rows, columns, and diagonals) using the 0-indexed positions.
tab=range(1,10): This range object is used to validate user input, ensuring the player chooses a number between 1 and 9.
🔄 Section 2: Core Game Functions
🔤 2.1 Printing the Board
def print\_board():
 """Prints the current state of the Tic-Tac-Toe board."""
 x=1
 for i in board:
 end = ' | '
 if x%3 == 0:
 end = ' \n'
 # Add separator line if not the last row
 if i != 1: end+='---------\n';
 char=' '
 # Display X, O, or the number if empty
 if i in ('X','O'): char=i;
 x+=1
 print(char,end=end)

This function iterates through the board list and prints each element.
It formats the output to resemble a 3x3 Tic-Tac-Toe grid, using ' | ' to separate cells and '\n' with '---------'for rows.
If a cell contains 'X' or 'O', it prints the character; otherwise, it prints a space, making it look empty.
Pro Tip: The end argument in print() prevents a new line after each item, allowing for horizontal printing.
🎲 2.2 Selecting Characters
def select\_char():
 """Randomly assigns 'X' or 'O' to the player and computer."""
 chars=('X','O')
 if random.randint(0,1) == 0:
 return chars[::-1] # Reverse order for computer
 return chars

This function uses random.randint(0,1) to randomly decide if the player gets 'X' or 'O'.
[::-1] is a slicing trick to reverse the tuple, ensuring the computer gets the other character.
✔️ 2.3 Checking for Valid Moves
def can\_move(brd, player\_char, move):
 """Checks if a move is valid (within board and spot is empty)."""
 if move in tab and brd[move-1] == move-1:
 return True
 return False

This function checks two conditions:
move in tab: Ensures the move (user input 1-9) is within the valid range.
brd[move-1] == move-1: Checks if the chosen spot on the board (adjusted for 0-indexing) is still empty (i.e., its content is still its original number).
🏆 2.4 Checking for Win Condition
def can\_win(brd, player\_char, move):
 """Checks if the current player can win with the given move."""
 places=[]
 x=0
 for i in brd:
 if i == player\_char: places.append(x);
 x+=1
 win=True
 for tup in winners:
 win=True
 for ix in tup:
 if brd[ix] != player\_char:
 win=False
 break
 if win == True:
 break
 return win

This function determines if a player has won.
It iterates through all winners combinations. For each combination, it checks if all three positions are occupied by the player\_char.
If a winning combination is found, it returns True; otherwise, it returns False.
➡️ 2.5 Making a Move
def make\_move(brd, player\_char, move, undo=False):
 """
 Attempts to make a move on the board.
 Returns (True, win\_status) if successful, (False, False) otherwise.
 If undo is True, the move is temporary (used for checking win conditions).
 """
 if can\_move(brd, player\_char, move):
 brd[move-1] = player\_char
 win=can\_win(brd, player\_char, move)
 if undo:
 brd[move-1] = move-1 # Revert the move if undo is true
 return (True, win)
 return (False, False)

This function attempts to place player\_char at the move position.
It first calls can\_move to ensure the move is valid.
If valid, it updates the board and then calls can\_win to check if this move results in a win.
The undo parameter is crucial for the AI's logic: when undo is True, the move is temporarily made and then immediately reverted, allowing the AI to "think ahead" without changing the actual game state.
🤖 2.6 Computer's AI Move
def computer\_move():
 """Determines the computer's move based on strategy (win, block, then corners/center/edges)."""
 move=-1
 
 # Strategy 1: Check if computer can win in the next move
 for i in range(1,10):
 if make\_move(board, computer, i, True)[1]: # Temporarily make move, check for win, then undo
 move=i
 break
 if move == -1:
 # Strategy 2: Check if player can win in the next move and block them
 for i in range(1,10):
 if make\_move(board, player, i, True)[1]: # Temporarily make player's potential winning move, then undo
 move=i
 break
 if move == -1:
 # Strategy 3: Prioritize moves based on a predefined order (corners, center, edges)
 for tup in moves:
 for mv in tup:
 if move == -1 and can\_move(board, computer, mv):
 move=mv
 break
 return make\_move(board, computer, move)

This function implements the computer's AI logic:
Winning Move: It first checks if there's any move the computer can make right now to win the game.
Blocking Move: If no winning move is found, it checks if the player can win on their next turn and, if so, it makes that blocking move.
Strategic Placement: If neither a winning nor a blocking move is available, the computer chooses a move based on the moves priority list (corners, then center, then edges).
It extensively uses make\_move with undo=True to simulate moves without altering the actual board until a decision is made.
🕳️ 2.7 Checking for Space Existence
def space\_exist():
 """Checks if there are any empty spaces left on the board."""
 return board.count('X') + board.count('O') != 9

This function checks if the sum of 'X's and 'O's on the board is less than 9. If it is, there are still empty spaces, and the game can continue. If it's 9, the board is full, indicating a draw unless someone has already won.
🕹️ Section 3: Game Flow
🚀 3.1 Game Start and Character Assignment
player, computer = select\_char()
print('Player is [%s] and computer is [%s]' % (player, computer))
result='%%% Deuce ! %%%' # Default result if game is a draw

Calls select\_char() to assign 'X' and 'O' to the player and computer.
Prints the assignment to the console.
Initializes result to a "Deuce" (draw) message, which will be updated if someone wins.
🎮 3.2 Main Game Loop
while space\_exist():
 print\_board()
 try:
 move = int(input('# Make your move ! [1-9] : '))
 except ValueError:
 print(' >> Invalid input ! Please enter a number between 1 and 9.')
 continue

 moved, won = make\_move(board, player, move)
 if not moved:
 print(' >> Invalid move ! Try again !')
 continue
 
 if won:
 result='*** Congratulations ! You won ! ***'
 break
 elif computer\_move()[1]: # Check if computer wins after its move
 result='=== You lose ! ==='
 break;

while space\_exist(): The game continues as long as there are empty spaces on the board.
print\_board(): Displays the current state of the board at the beginning of each turn.
move = int(input(...)): Prompts the player for their move (1-9) and converts the input to an integer.
try-except ValueError: This block handles cases where the user enters non-numeric input, preventing the program from crashing.
moved, won = make\_move(board, player, move): Attempts the player's move. moved is True if the move was valid. won is True if the player won with this move.
if not moved:: If the player's move was invalid, an error message is printed, and the loop continues to the next iteration, prompting the player again.
if won:: If the player wins, the result is updated, and the loop breaks.
elif computer\_move()[1]:: If the player didn't win, the computer makes its move. computer\_move() also returns a (moved, won) tuple. We check the won status ([1] index) for the computer. If the computer wins, the result is updated, and the loop breaks.
🏁 3.3 Game End
print\_board()
print(result)

After the loop breaks (due to a win or a draw), the final board state is printed.
The result message (win, lose, or deuce) is printed to the console.
💡 Bonus Tips & Challenge Tasks
Beginner: Change the characters used (e.g., emojis). Customize win/lose messages.
Intermediate: Implement a reset\_game() function to play multiple rounds without restarting the script. Add a score tracker.
Advanced: Improve the computer AI to be unbeatable (e.g., using the minimax algorithm). Create a GUI for Tic-Tac-Toe using tkinter or another library.