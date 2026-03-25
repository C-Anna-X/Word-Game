''' 
This program creates the game Lingo. In this game the computer chooses 
a five letter secret word then prompts the user to guess the word. The 
game ends if the user types in "QUIT" or gets the word correct. At each
turn the computer will return which letters are an exact match or inexact match.

Siana Lai
October 31, 2025
'''

from getWords import getWords
from random import choice

def main():
    printIntro()
    allwords = getWords()

    secret = genSecretTarget(allwords)

    number_guesses = 0 
    while True: 
        guess = getGuess(allwords)

        if guess is None:
            print(f'The secret word was: {secret}.')
            print('Better luck next time!')
            return None
        else: 
            printStatus(guess, secret)
            number_guesses += 1
            if guess == secret:
                break

    if number_guesses == 1:
        print(f'You guessed the word {guess} in {number_guesses} turn.')
        print('Congratulations!')
    else:
        print(f'You guessed the word {guess} in {number_guesses} turns.')
        print('Congratulations!')



def printIntro():
    '''Prints instructions for the game'''
    print(f'''@@@@@@@@@@@@@@@@@@@@@@@
          Welcome to Lingo!
            Each turn you will try to guess the secret word
            If you guess the word, you win
            If you guess some letters in the word, lingo will display:
                guessed letters n the correct position in upper case
                guessed letters in the incorrect position in lower case
            If you want to end the game type "QUIT" and hit enter. 
        Good Luck!
        @@@@@@@@@@@@@@@@@@@@@@@@@''')
    print("word: - - - - -")


def genSecretTarget(allwords: list[str]) -> str:
    ''' Takes one input parameter and returns a string containing target word'''

    secret_target = choice(allwords)
    return secret_target

def getGuess(allWords: str) -> str:
    '''Gets valid guesses from user, prompting as many times as necessary.
    returns the guessed string. Guess is valid if it appears in allWords.
    Typing "QUIT" to end the game. '''

    while True: 
        user_guess = (input('Enter a 5 letter word:'))
        if user_guess == "QUIT":
            return None
        
        user_guess_lower = user_guess.lower()
        if user_guess_lower in allWords:
            return user_guess_lower

        else:
            print('Please try again, enter a valid 5 letter word:')

def printStatus(guess: str, secret: str) -> None: 
    '''Computes exact and inexact matches then prints current status to screen.'''

    statusList = list(guess)
    secretList = list(secret)
    exactMatch(statusList, secretList)
    inexactMatch(statusList, secretList)
    current_status = " ".join(statusList)
    print(current_status)

def exactMatch(statusList: list, secretList: list) -> None:
    '''Given two lists of five characters each, computes exact matches between two lists
    converting the exact matches in statusList to uppercase. Replace the corresponding
    match in secretList with "." .'''

    for i in range(len(statusList)):
        if statusList[i] == secretList[i]:
            statusList[i] = statusList[i].upper()
            secretList[i] = '.'

def inexactMatch(statusList: list, secretList: list) -> None:
    '''Given two lists of five characters each, computes inexact matches between two lists
    replacing corresponding match in statusList with "." . If not an inexact match, replace
    letter with "-" in statusList.'''
    
    for i in range(len(statusList)):
        if statusList[i].isupper():
            continue

        ch = statusList[i]
        found = False

        for j in range(len(secretList)):
            if secretList[j] == ch:
                secretList[j] ='.'
                found = True

        if not found: 
            statusList[i] = "-"


main()
