import random
import sys,os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
name=''
missing = ''
correct = ''
secret = ''
gameDone = False




from  game.gamestate import gamestate

from  leaderboard.leaderboard import leaderboard

def getRandomWord():
    wordslist = ['rose', 'jasmine', 'lily', 'hibiscus', 'mariegold', 'diasy', 'tulip', 'sunflower',
             'lotus', 'pancy', 'dahlia', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

    w = random.choice(wordslist)
    return w


def worddisplayBoard(hang, miss, correct, secret):
    print(hang[len(missing)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missing:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secret)

    for i in range(len(secret)):  # replace blanks with correctly guessed letters
        if secret[i] in correct:
            blanks = blanks[:i] + secret[i] + blanks[i+1:]

    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print("\n")


def getGuesses(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def Againplay():
    return input("\nDo you want to play again? ").lower().startswith('y')
































def main_code(leaderboard_obj,gamestate_obj):

 hang = ["""
  H A N G M A N 

   +---+
   |   |
       |
       |
       |
       |
  =========""", """
  H A N G M A N 

  +---+
  |   |
  O   |
      |
      |
      | 
  =========""", """
  H A N G M A N 

  +---+
  |   |
  O   |
  |   |
      |
      | 
  =========""", """
 H A N G M A N 

   +---+
   |   |
   O   |
  /|   |
      |
      |
  =========""", """
  H A N G M A N 

  +---+
  |   |
  O   |
 /|\  |
      |
      |
  =========""", """
  H A N G M A N 

  +---+
   |   |
   O   |
  /|\  |
  /    |
      |
  =========""", """ 
  H A N G M A N 

   +---+
   |   |
   O   |
  /|\  |
  / \  |
      |
  ========="""]
 name=input("Enter your name : ")
 
 
 missing = ''
 correct = ''
 secret = getRandomWord()
 gameDone = False

 while True:
    worddisplayBoard(hang, missing, correct, secret)

    guess = getGuesses(missing + correct)

    if guess in secret:
        correct = correct + guess

        foundAllLetters = True
        for i in range(len(secret)):
            if secret[i] not in correct:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('\nYes! The secret word is "' +
                  secret + '"! You have won!')
            leaderboard_obj.game_update_leaderboard({'name':name,'game_name':'hangman','points':100,'duration':'10mins'})
            gameDone = True
    else:
        missing = missing + guess

        if len(missing) == len(hang) - 1:
            worddisplayBoard(hang, missing,
                         correct, secret)
            print('You have run out of guesses!\nAfter ' + str(len(missing)) + ' missed guesses and ' +
                  str(len(correct)) + ' correct guesses, the word was "' + secret + '"')
            gameDone = True

    if gameDone:
        if Againplay():
            missing = ''
            correct = ''
            gameDone = False
            secret = getRandomWord()
        else:
            return leaderboard_obj
            break
