#manohar



import random
import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from  game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard


name='input("Enter your name : ")'


board = [i for i in range(0, 9)]
player, Ai = '', ''
tab = range(1, 10)

gamestate_object={'name':name,'game_name':'tic tac toe','points':0,'duration':''}
 
gamestate=gamestate() 
   

actions = ((1, 7, 3, 9), (5,), (2, 4, 6, 8)) 

winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def print_board():
    x = 1
    for i in board:
        end2 = ' | '
        if x % 3 == 0:
            end2 = ' \n'
            if i != 1: 
                 end2 += '---------\n'
        char = ' '
        if i in ('X', 'O'):
             char = i
        x += 1
        print(char, end=end2)


def select_char():
    chars = ('X', 'O')
    if random.randint(0, 1) == 0:
        return chars[::-1]
    return chars


def can_action(brd, player, move):
    if move in tab and brd[move - 1] == move - 1:
        return True
    return False


def can_win(brd, player, move):
    places = []
    x = 0
    for i in brd:
        if i == player: 
            places.append(x)
        x += 1
    win = True
    for tup in winners:
        win = True
        for ix in tup:
            if brd[ix] != player:
                win = False
                break
        if win == True:
            break
    return win


def do_action(brd, player, move, undo=False):
    if can_action(brd, player, move):
        brd[move - 1] = player
        win = can_win(brd, player, move)
        if undo:
            brd[move - 1] = move - 1
        return (True, win)
    return (False, False)


# AI goes here
def Ai_action():
    action = -1

    for i in range(1, 10):
        if do_action(board, Ai, i, True)[1]:
            action = i
            break
    if action== -1:

        for i in range(1, 10):
            if do_action(board, player, i, True)[1]:
                action = i
                break
    if action == -1:
        
        for tup in actions:
            for mv in tup:
                if action == -1 and can_action(board, Ai, mv):
                    action = mv
                    break
    return do_action(board, Ai, action)


def space_exist():
    return board.count('X') + board.count('O') != 9


player, Ai = select_char()


def main_code(leaderboard_obj,gamestate_object):
 name=input("Enter your name : ")
 gamestate_object['name']=name
 gamestate_object['game_name']='tic tac toe'
 gamestate_object['duration']='5mins'
 
 print('Player is [%s] and computer is [%s]' % (player, Ai))
 result = '%%%  Game tied ! %%%'
 while space_exist():
    print_board()
    print('# Make your move ! [1-9] : ', end='')
    move = int(input())
    moved, won = do_action(board, player, move)
    if not moved:
        print(' >> Invalid number ! Try again !')
        continue
    #
    if won:
        result = '*** HOOrah ! You won !***'
        gamestate_object['points']+=100
        
        gamestate.update(gameobject=gamestate_object)
        leaderboard_obj.game_update_leaderboard(gamestate.gamestate)
        break
    elif Ai_action()[1]:
        result = '=== You lose ! =='
        break

 print_board()
 print(result)
 print(leaderboard_obj.leaderboard)
 return leaderboard_obj
