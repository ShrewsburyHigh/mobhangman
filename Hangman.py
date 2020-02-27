from __future__ import print_function 
import turtle
import time
lives = 6
word = ""
letter = ""
updatedSpaces= []

def intialize ():
    global word
    global updatedSpaces
    word = "airport"
    updatedSpaces = "_ _ _ _ _ _ _"
    print("Try to guess the word in 6 tries")
    print(updatedSpaces)

def getLetter():
    global letter
    print("What is your guess?")
    letter = input()
    check()
   
def won():
    if updatedSpaces == word:
        print("Hurray, you got the word!")
    else:
        getLetter()        
def check():
    global updatedSpaces
    global lives
    if letter in word:
        index = -1
        for i in word:
            index += 1
            if letter == i:
                updatedSpaces[index] = letter
            else:
                continue
        print (' '.join(updatedSpaces))
        won()     
    else: 
        lives -= 1
        if lives == 0:
            print('You loser')
        else:
            getLetter()
        
 
def main():
    intialize()
    getLetter()
    check()
    
main()
