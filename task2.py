"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
def title():
    print('Number Guessing Game\nInstruction : AI will give you a inter number that round of 1-10\nYou need to enter a number')
    print('If the enter number is same as the number that AI give to you, then you win this game')
import random
a = round(random.uniform(1,10))

def game():

  i = input('Enter a number between 1-10:')
  if i == a:
     print(" Congratulation, You win")
  if i != a:
     print(f'The give number is {a} ')
     print('You lost, next time')

title()

game()
