## 1. ❌⭕ Tic-Tac-Toe Game

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
