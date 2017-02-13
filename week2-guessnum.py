# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("Please think of a number between 0 and 100! ")

numlow = 0
numhig = 100
guessed = False

# loop until we guess correctly
while not guessed:
    numguess = (numlow + numhig)//2    
    print("Is your secret number " + str(numguess) + "?")
    guessmark = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if guessmark == 'h':
        numhig = (numlow+numhig)//2
    elif guessmark == 'l':
        numlow = (numlow+numhig)//2
    elif guessmark == 'c':  
        print("Game over. Your secret number was : ", numguess)
    else:
        print("Sorry, I did not understand  your input.")
