###############################################################################
#                       Project 1 - Snake & Ladders                           #
###############################################################################
# * --------------------------------------------------------------------------*
# *    * @author  : ankit sharma
        # @description : snake and ladder multiplayer code
# *   *
# *   *
# * --------------------------------------------------------------------------*
# *                                           *
# * ************************************************************************"""

# Importing Libraries
import random


import sys,os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))





from  game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard
gamestate_obj= gamestate()

leaderboard_obj=leaderboard()
# Snake Class
class Snake:
    """
    Class to Implement Snakes and Ladders Game.
    """

    # Default Constructor
    def __init__(self):

        print("###### Welcome to Snakes & Ladders Game ######")
        self.name = input("Enter the Name of Player 1 : ")
        self.comp = input("Enter the Name of Player 2 : ")
        print("###### Let us Start ######")
        self._game = [0, 0]  # Steps of the Players [Initial]

        # Goto Dictionaries [Given the Question]
        self.__pos_of_snakes = {
    8: 4,
    18: 1,
    26: 10,
    39: 5,
    51: 6,
    54: 36,
    56: 1,
    60: 23,
    75: 28,
    83: 45,
    85: 59,
    90: 48,
    92: 25,
    97: 87,
    99: 63
}
        self.__pos_of_ladders ={
    3: 20,
    6: 14,
    11: 28,
    15: 34,
    17: 74,
    22: 37,
    38: 59,
    49: 67,
    57: 76,
    61: 78,
    73: 86,
    81: 98,
    88: 91
}


    # Display Players' Name
    def displayName(self):

        print("Player 1's Name : {}, Player 2's Name : {}".format(self.name, self.comp))

    # Display Winner's Name
    def __displayWinner(self, number):

        if number == "1":
            winner = self.name
            leaderboard_obj.addplayer({'name':self.name,'game_name':'snake and ladder ', 'points':100,'duration':'15 mins'})


        else:
            winner = self.comp
            leaderboard_obj.addplayer({'name':self.comp,'game_name':'snake and ladder ', 'points':100,'duration':'15 mins'})

        print("Player {} won the Game!".format(number))
        print("Congratulations {} !!".format(winner))
        
        print("###### Game Successfully Finished ######")
        exit(0)

    # Check for Any Snakes or Ladders in the current position
    def __checkSnakeLadder(self, position):

        if position in self.__pos_of_snakes.keys():
            position = self.__pos_of_snakes.get(position)
        elif position in self.__pos_of_ladders.keys():
            position = self.__pos_of_ladders.get(position)
        return position

    # Check for 'quit'
    def __quitGame(self, number):

        if number == "1":
            self.__displayWinner("2")
        else:
            self.__displayWinner("1")
        exit(0)

    # Check for Overflow Position
    def __checkMoreThanHundred(self, position, x):

        if (position + x) > 100:
            pass  # Check for > 100
        else:
            position += x
        return position

    # Check for the Range of Input in Manual Mode
    def __checkManualMode(self, inp):

        x = int(inp)
        if x not in range(0, 7):
            print("Invalid Input! The Number you Entered isn't within the range of between 1 and 6")
            x = int(input("Please Enter a Number within the given Range : "))
        return x

    # Check for the Move Input if it's Valid or Illegal
    def __checkMoveInput(self, number):

        inp = input("Player {} : ".format(number))
        if inp == "roll":  # Auto [Automatic]
            x = random.randint(1, 6)
        elif inp == "quit":
            self.__quitGame(number)
        elif inp.isnumeric():  # Manual [Betwen 1-20]
            x = self.__checkManualMode(inp)
        else:
            print("Illegal Input, Please Input a Valid Input!")
            x = self.__checkMoveInput(number)
        print("You got a ", x)
        return x

    # Player Position Function
    def __playerPosition(self, number):

        pos = 0
        pos = self._game[int(number) - 1]
        x = self.__checkMoveInput(number)  # Check for Valid Input
        pos = self.__checkMoreThanHundred(pos, x)  # Check for the Validity of the Position
        pos = self.__checkSnakeLadder(pos)  # Check for Snakes and Ladder
        print(" Your Final Position is ", pos)
        if pos == 100:  # Check for Winner
            self.__displayWinner(number)
        self._game[int(number) - 1] = pos  # Lastly assigning the step into the list

    # Snake Game Function
    def snakeGame(self):

        while True:
            self.__playerPosition('1')
            self.__playerPosition('2')


# Main Method
def main_code():
    #self.name = 'input("Enter the Name of Player 1 : ")'
    #elf.comp = 'input("Enter the Name of Player 2 : ")'
    # Using Exception Handling Techniques to Handle any unfavourable outcomes
    snake = Snake()
    # snake.displayName()
    snake.snakeGame()  # Game Method
    del snake  # Delete the Object

###############################################################################
#                                 END                                         #
###############################################################################