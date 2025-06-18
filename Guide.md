# 🐍 Consolidated Python Game Guide(DCSI 2025-Jun 18) 🎮 ~ Ryan Fernandes

This document combines a teaching guide for three beginner-friendly Python games:
- Hangman
- Mad Libs
- Tic-Tac-Toe

Each section includes annotated code, concepts, and bonus challenges.

---

## 1. 🔤 Hangman Game

### 🎯 Objective
Learn:
- Input/output
- Loops and conditionals
- Strings and logic
- Using modules like `time`

### 🧩 Import Required Module
```python
import time
```
time.sleep() pauses the program — like saying “Hold on a second!” to the computer.

### 💬 Ask for the User's Name
```python
name = input("What is your name? ")
print(f"Hello, {name}! Time to play hangman!")
```
### 🕓 Add Some Drama
```python
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
```
### 🔐 Set the Secret Word
```python
word = "Danger"
guesses = ''
turns = 10
```
### 🔁 Main Game Loop
```python
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=' ')
        else:
            print("_", end=' ')
            failed += 1
    if failed == 0:
        print("You won")
        break
```
### 🔡 Player’s Guess
```python
guess = input("guess a character: ")
guesses += guess
```
### ❌ Wrong Guess Handling
```python
if guess not in word:
    turns -= 1
    print("Wrong")
    print(f"You have {turns} more guesses")
```
### 💀 Loss Condition
```python
if turns == 0:
    print("You Lose")
```
### 💡 Bonus Challenges
Beginner: Customize words/messages
Intermediate: Add scoring or input validation
Advanced: ASCII art, difficulty levels, random words
## 2. 🧠 Mad Libs Game

### 🎯 Objective
Collect multiple user inputs
Concatenate inputs into a story
Build a GUI using tkinter
### 🧩 Import Tkinter and Inputs
```python
from tkinter import *

adjective1 = input("Tell me an adjective: ")
noun1 = input("Tell me a noun (plural): ")
adjective2 = input("Tell me another adjective: ")
noun2 = input("Another noun: ")
verb = input("Tell me a verb: ")
```
### 📣 Welcome Message
```python
print("Welcome to Mad Libs! Let's start")
```
### 🖼️ Create the GUI Window
```python
master = Tk()
master.title('Mad Libs')
master.minsize(width=400, height=400)
```
### 📜 Build and Display the Story
```python
x = adjective1
y = noun1
z = adjective2
a = noun2
b = verb

story = f"There was once a {x} boy from Dubai\n" \
        f"who was baked by {y} in a pie\n" \
        f"to his {z}'s {a} disgust\n" \
        f"he {b} through the crust\n" \
        f"and exclaimed, 'what a good boy am I!'"

w = Label(master, text=story)
w.pack()
mainloop()
```
### 💡 Bonus Challenges
Beginner: Add more word inputs
Intermediate: Use f-strings; add Reset button
Advanced: Organize with Frames; input validation
## 3. ❌⭕ Tic-Tac-Toe Game

### 🎯 Objective
Build board using a list
Create player/computer logic
Implement win and draw detection
### 🧩 Setup and Board Representation
```python
import random
board = [i for i in range(0,9)]
player, computer = '', ''
```
### ✔️ Assign Characters
```python
def select_char():
    return ('X', 'O') if random.randint(0, 1) else ('O', 'X')
```
### 📏 Board Display
```python
def print_board():
    x = 1
    for i in board:
        end = ' | '
        if x % 3 == 0:
            end = '\n'
            if i != 1:
                end += '---------\n'
        char = i if i in ('X', 'O') else ' '
        print(char, end=end)
        x += 1
```
### 🧠 Move Logic
```python
def can_move(brd, player_char, move):
    return move in range(1,10) and brd[move-1] == move-1

def can_win(brd, player_char, move):
    winners = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(all(brd[i] == player_char for i in combo) for combo in winners)
```
### 🤖 Computer Move
```python
def computer_move():
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            return make_move(board, computer, i)
    for i in range(1, 10):
        if make_move(board, player, i, True)[1]:
            return make_move(board, computer, i)
    for mv in [1,7,3,9,5,2,4,6,8]:
        if can_move(board, computer, mv):
            return make_move(board, computer, mv)
```
### 🕹️ Main Game Loop
```python
player, computer = select_char()
print(f"Player is [{player}] and computer is [{computer}]")

while board.count('X') + board.count('O') != 9:
    print_board()
    try:
        move = int(input("Your move [1-9]: "))
    except ValueError:
        print("Invalid input!")
        continue

    moved, won = make_move(board, player, move)
    if not moved:
        print("Invalid move!")
        continue
    if won:
        print("*** You won! ***")
        break
    elif computer_move()[1]:
        print("=== You lose! ===")
        break
```
### 💡 Bonus Challenges
Beginner: Use emojis for pieces 
Intermediate: Add scoreboard, replay
Advanced: GUI version, unbeatable AI (minimax)
## 📌 Summary

Game	Concepts Covered
Hangman	Strings, loops, logic, input/output
Mad Libs	Input, string formatting, GUI with Tkinter
Tic-Tac-Toe	Lists, win-checking, AI, user validation
