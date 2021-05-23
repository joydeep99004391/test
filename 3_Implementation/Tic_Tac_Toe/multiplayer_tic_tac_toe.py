
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard

board=['0','1','2','3','4','5','6','7','8']
empty = [0,1,2,3,4,5,6,7,8]
name1='input("Enter your name player1 : ")'
name2='input("Enter your name player2 : ")'
multiplayer_obj={'player_list':[name1,name2],'winner':'','points_changed':100}
#leaderboardobj=leaderboard()
#leaderboardobj.updategamefortwoplayers(multiplayer_obj)
#function to display board
def display_board():
  print('  |   |   ')
  print(board[0]+' | '+board[1]+' | '+board[2])
  print('  |   |   ')
  print('---------')
  print('  |   |   ')
  print(board[3]+' | '+board[4]+' | '+board[5])
  print('  |   |   ')
  print('---------')
  print('  |   |   ')
  print(board[6]+' | '+board[7]+' | '+board[8])
  print('  |   |   ')


def player_input(player):
    player_symbol = ['X', 'O']
    correct_input = True

    position = int(input('player {playerNo} chance! Choose field to fill {symbol} '.format(playerNo=player + 1,
                                                                                           symbol=player_symbol[
                                                                                               player])))

    if board[position] == 'X' or board[position] == 'O':
        correct_input = False

    if not correct_input:
        print("Position already equipped")
        player_input(player)
    else:
        empty.remove(position)
        board[position] = player_symbol[player]
        return 1
def check_win():
  #define players symbols and winning positions
  player_symbol = ['X','O']
  winning_positions =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

  #check all winning positions for matching placements
  for check in winning_positions:
    first_symbol = board[check[0]]
    if first_symbol != ' ':
      won = True
      for point in check:
        if board[point] !=  first_symbol:
          won = False
          break
      if won:
        if first_symbol == player_symbol[0]:
          print('player 1 won')
          multiplayer_obj['winner']=multiplayer_obj['player_list'][0]
        else:
          print('player 2 won')
          multiplayer_obj['winner']=multiplayer_obj['player_list'][1]
        break
    else:
      won = False

  if won:
    return 0
  else:
    return 1
def play():
  player = 0
  while empty and check_win():
    display_board()
    player_input(player)
    player = int(not player)
  if not empty:
    print("NO WINNER!")

#driver code
def main_code(leaderboardobj,gamestate_obj):
  name1=input("Enter your name for 1st player: ")
  name2=input("Enter your name for 2nd player: ")
  multiplayer_obj['player_list']=[name1,name2]

  play()
  
  leaderboardobj.updategamefortwoplayers(multiplayer_obj)
  print(leaderboardobj.leaderboard)
  return leaderboardobj
