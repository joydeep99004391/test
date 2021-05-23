

# TEST PLAN:

## Table 1: High Level Test Plan

| **Test ID** | **Description**                                              | **Exp I/P** | **Exp O/P** | **Actual O/P** |**Type Of Test**  |    
|-------------|--------------------------------------------------------------|------------|-------------|----------------|------------------|
| H_001 | Leaderboard | Integer | Integer | ** | Requirement based |
| H_002 | Add or Removal Games | Integer | Integer | ** | Requirement based |
| H_003 | Exporting data in to file | Integer | Integer | ** | Requirement based |
| H_004 | System Performance | Integer | Integer | ** | Technical based |
| H_005 | Multiplayer | Integer | Integer | ** | Technical based |





## Table 2: Low Level Test Plan

| **Test ID** | **HLT ID** | **Description**                                              | **Exp IN** | **Exp OUT** | **Actual Out** |**Type Of Test**  |    
|-------------|-----|--------------------------------------------------------------|------------|-------------|----------------|------------------|
|  L_011  | H_001 | The scores must automatically get sorted after each game| Integers| ** | ** | Technical |
|  L_012  | H_001 | Show stats of each player i.e wins,losses,points in every game| Integers| ** | ** | Technical |
|  L_013  | H_001 | Ask name details of each player before starting the game| Integers| ** | ** | Technical |
|  L_014  | H_001 | Stats of both the players playing against each other must be displayed while playing| Integers| ** | ** | Technical |
|  L_021  | H_002 | Acess of adding or removal of game from the menu will be only with admin| Integers| ** | ** | Technical |
|  L_022  | H_002 |Less Participation Games will be removed by Admin| Integers | ** | ** | Technical |
|  L_023  | H_002,H_001 |  If the games was removed the points gained from that game will also be removed in leaderboard.| Integers| ** | ** | Technical |
|  L_024  | H_002,H_001 |Seperate leaderboard between two players beside main leaderboard.| Integers | ** | ** | Technical |
|  L_031  | H_003 | A file stored with user win/ losses recoreds| Integers| ** | ** | Technical |
|  L_032  | H_003 | Writing the name of the users and their game stats of each player for each game into file| Integers| ** | ** | Technical |
|  L_033  | H_003 | Updating game stats of each player i.e wins/loss and point earned at the end of each game| Integers| ** | ** | Technical |
|  L_034  | H_003 | Creating a unique csv file to each user with his game stats.| Integers| ** | ** | Technical |
|  L_041  | H_004 |Package Download | Integers | ** | ** | Technical |
|  L_042  | H_004 |Clean Old Data | Integers | ** | ** | Technical |
|  L_043  | H_004 |Update Old Files | Integers | ** | ** | Technical |
|  L_045  | H_005 |Single Player can play online | Integers | ** | ** | Technical |
|  L_046  | H_005 |Player can invite others | Integers | ** | ** | Technical |
|  L_047  | H_005 |Two players can play as many games as after one another | Integers | ** | ** | Technical |
|  L_048  | H_005 |Chat option will be enabled for players while playing | Integers | ** | ** | Technical |

