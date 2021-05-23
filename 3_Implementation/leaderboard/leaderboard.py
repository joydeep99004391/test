


'''

@author:joydeep99004391
@description: leaderboard class which defines fucntions for the leaderboard 


'''


class leaderboard:

          leaderboard=[]
          current_state_leaderboard={}
          def __init__(self):
               emptyleaderboard=[{'name':"name of player", 'points':"points of player",'duration':"duration of game played",'last_game_played':''}]
               self.leaderboard=emptyleaderboard
          def addplayer(self,gameobject):                              
                           self.leaderboard.append({'name':gameobject['name'],'last_game_played':gameobject['game_name'],'points':gameobject['points'],'duration':gameobject['duration']})
          def updategamefortwoplayers(self,multiplyerobj):
                                 # function to update the leaderboard for multiplayer between two objects  
                                 player_list=multiplyerobj['player_list']
                                
                                 for i in player_list:
                                         for j in range(len(self.leaderboard)):
                                              
                                                         if self.leaderboard[j]['name']==i :  
                                              
                                                                      if multiplyerobj['winner'] ==  i:
                                                                                      self.leaderboard[j]['points'] += multiplyerobj['points_changed']                                 
                                                         else : 
                                                               if multiplyerobj['winner'] == i:
                                                                   self.addplayer({'name':i,'game_name':'tic tac toe','points':100 ,'duration':'5mins' }) 
                                                                  
          def deletepoints(self,deleteobj):
                           '''  function to delete points from players either by admin or system automatically 
                           ''' 
                           playerlist_deleted=deleteobj['player_list']
                           for j in playerlist_deleted:
                            for i in self.leaderboard : 
                                       if i['name'] == j: 
                                                 i['points'] -= playerlist_deleted['points_deleted']
                                                 #self.leaderboard[self.leaderboard.index(i)]['points']-=playerlist_deleted['points_deleted']
                           self.leaderboard=self.leaderboard                     
          def export_leaderboard(self):
                    return self.leaderboard    
          def game_update_leaderboard(self,gameobject):
                          
                         
                         
                         for i in self.leaderboard:
                                            if i['name']==gameobject['name']:
                                                           i['points']+=gameobject['points']
                                                           i['duration']=gameobject['duration']
                                                           i['last_game_played']=gameobject['game_name']
                                            else: 
                                                  self.addplayer(gameobject)                                  


                                          