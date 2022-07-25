"""
Steps to make the game: 
1. borad
2. display board
3. handle turn
4. check win
    4.1. check rows
    4.2. check columns
    4.3. check diagonal
5.check tie
6.flip player
7. play game
"""
# global variables
game_on = True
Winner = None
cp = "X"
# making board
board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
# display board
def dis_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# handling turns of the two players 
def handle_turn(player):
  print(player + "'s Turn.")
  pos = input("Choose a position from 1-9: ")
  valid = False
  while not valid:
    while pos not in ["1","2","3","4","5","6","7","8","9"]:
      pos = input("Invalid Input. Choose again from 1-9: ")
    pos = int(pos) - 1
    if board[pos] == "-":
      valid = True
    else:
      print("Can't go there. Choose Again")
  board[pos] = player
  # displaying the board
  dis_board()

  # checking if the game has ended or not
def game_off():
  if_win()
  if_tie()
# checking if somebody won
def if_win():
  global Winner
  # check rows
  rw = check_rows()
  # check columns
  cw = check_columns()
  # check diagonals
  dw = check_diagonals()
  # Winner!!
  if rw:
    Winner = rw
  elif cw:
    Winner = cw
  elif dw:
    Winner = dw
  else:
    Winner = None
  return

def check_rows():
  global game_on
  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"
  if row1 or row2 or row3:
    game_on = False
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[6]
  return

def check_columns():
  global game_on
  col1 = board[0] == board[3] == board[6] != "-"
  col2 = board[1] == board[4] == board[7] != "-"
  col3 = board[2] == board[5] == board[8] != "-"
  if col1 or col2 or col3:
    game_on = False
  if col1:
    return board[0]
  elif col2:
    return board[1]
  elif col3:
    return board[2]
  return

def check_diagonals():
  global game_on
  d1 = board[0] == board[4] == board[8] != "-"
  d2 = board[2] == board[4] == board[6] != "-"
  if d1 or d2:
    game_on = False
  if d1:
    return board[0]
  elif d2:
    return board[2]
  return
# checking if there is a tie.
def if_tie():
  global game_on
  if "-" not in board:
    game_on = False
  return
# fliping the chance of players
def flip_player():
  global cp
  if cp == "X":
    cp = "O"
  elif cp == "O":
    cp = "X"
  return

  # Assembling all the function to play Tic-Tac-Toe
def play_game():
  dis_board()
  # while game is till on
  while game_on:
    # handle a single turn of arbitrary player
    handle_turn(cp)
    # Check if Game has Ended
    game_off()
    # Flip to another player
    flip_player()
  # Game Ended
  if Winner == "X" or Winner == "O":
    print(Winner + " won!!")
  elif Winner == None:
    print("Tie.")

# Final game:-  "Tic-Tac-Toe"
while True:
  ch = input("Want to play Tic-Tac-Toe(Y/N): ")
  if ch == "Y" or ch == "y":
    print("Let's Play!!")
    play_game()
  elif ch == "n" or ch =="N":
    print("Thanks for Playing.")
    break
  else:
    print("Wrong choice. Pick again")