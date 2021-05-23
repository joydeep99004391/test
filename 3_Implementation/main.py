
import sys
import os

PACKAGE_PARENT = '.'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard


from Tic_Tac_Toe.player_vs_comp import main_code as tic_tac_toe_main_single


from Tic_Tac_Toe.multiplayer_tic_tac_toe import main_code as tic_tac_toe_main_multi



from SnakeLadder.snakeladder import main_code as snake_ladder_single


from SnakeLadder.Multiusersnakeladder import main_code as snake_ladder_multi

from Hangman.hangman import main_code as hangman_single

from export_data.export_import  import write_file


from export_data.export_import  import read_file






gamestate_obj= gamestate()

leaderboard_obj=leaderboard()
if __name__=='__main__':
           print("1.tic tac toe   \n 2 snake ladder \n 3. hangman ")
           choice=int(input())
           choice2=0
           if choice == 1 :
                       print("  1. single player \n 2. multiplayer") 
                       choice2=int(input())
                       if choice2 ==1:
                            leaderboard_obj=    tic_tac_toe_main_single(leaderboard_obj,gamestate_obj.gamestate)
                            write_file(leaderboard_obj.leaderboard)  
                       elif choice2 == 2 : 
                            leaderboard_obj=       tic_tac_toe_main_multi(leaderboard_obj,gamestate_obj.gamestate)  
                            write_file(leaderboard_obj.leaderboard)      
           if choice == 2 :
                       print("  1. single player \n 2. multiplayer") 
                       choice2=int(input())
                       if choice2 ==1:
                                leaderboard_obj=snake_ladder_single()
                                write_file(leaderboard_obj.leaderboard)
                       elif choice2 == 2 : 
                                   leaderboard_obj=snake_ladder_multi()  
                                   write_file(leaderboard_obj.leaderboard)
           if choice == 3 :
                       print("  1. single player \n 2. multiplayer") 
                       choice2=int(input())
                       if choice2 ==1:
                             leaderboard_obj=  hangman_single(leaderboard_obj,gamestate_obj)
                             write_file(leaderboard_obj.leaderboard)
                       elif choice2 == 2 : 
                                  leaderboard_obj= snake_ladder_multi(leaderboard_obj,gamestate_obj)   
                                  write_file(leaderboard_obj)  
                                                                                     
                         