'''

@author:joydeep99004391
@description: gamestate class which refers to the current gamestate 


'''





class gamestate:
          gamestate={'name':'','game_name':'','points':'','duration':''}

          previousgamestate=gamestate
          
          def __init__(self) -> None:
               gamestatedict={'name':'','game_name':'','points':0,'duration':''}
               self.gamestate=gamestatedict
               self.previousgamestate=gamestatedict
               
          def update(self,gameobject):
                           currentstate=self.get_game_state()
                           prevousgamestate=currentstate
                           
                           self.gamestate= {'name':gameobject['name'],'game_name':gameobject['game_name'],'points':gameobject['points'],'duration':gameobject['duration']}
                           

          def get_game_state(self):
                            return self.gamestate  

          def rollbackpreviousupdate(self):
                 self.gamestate=self.previousgamestate
                                   
          
