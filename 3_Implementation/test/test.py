
import sys,os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


from  game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard

from export_data.export_import import write_file
from export_data.export_import import read_file


leaderboard_obj_global=leaderboard()


def test_add_player():
   leaderboard_obj=leaderboard()
   leaderboard_obj.addplayer({'name':'test','game_name':'test_game','points':100,'duration':'30 mins'}) 
   
   assert len(leaderboard_obj.leaderboard) > 1




def test_game_update_leaderboard():
       leaderboard_obj=leaderboard()
       leaderboard_obj.game_update_leaderboard({'name':'test','game_name':'test_game','points':100,'duration':'30 mins'}) 
   
       assert len(leaderboard_obj.leaderboard) > 1



def test_update_game_for_two_players():
     multiplayer_obj={'player_list':['test1','test2'],'winner':'test1','points_changed':100}
     leaderboard_obj_global.updategamefortwoplayers(multiplayer_obj)

def test_export_Data():
     return_val=write_file([{'name':'test','game_name':'test_game','points':100,'duration':'30 mins'}])
     assert return_val ==0

def test_import_Data():
     str_buffer=read_file()
     assert len(str_buffer)>0

