import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard


#gamestate_leaderboard=leaderboard
#current_leaderboard=gamestate_leaderboard.export_leaderboard()



def write_file(current_leaderboard):
        filename='../w.txt'


        f=open(filename,'w',encoding='utf-8')
        #print('@###',current_leaderboard)
        f.write('HERE IS THE LEADERBOARD \n')
        for i in current_leaderboard:
               f.write(str(i)+"\n")
        f.close()     
        return 0

      
       




def read_file():
        filename='../w.txt'


        f=open(filename,'r',encoding='utf-8')
        readbuffer=f.read()
        readbuffer.split('\n')
        f.close()
        return readbuffer


      