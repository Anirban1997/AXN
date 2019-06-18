# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:56:44 2019

@author: anirbanmandol
"""
import random
num = random.randint(1,100)
guesses = [0]
print("Welcome to GUESS ME")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

while True:
    guess = int(input("I'm thinking a number between 1 to 100.what is your guess?"))
    if guess<0 or guess>100:
        print("Out of bounds! plase try agaiin.")
        continue
    
    if guess == num:
        print(f"Congtrats you have took only {len(guesses)} chance.")
        break
    guesses.append(guess)
    
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("Warmer")
        else:
            print("Colder")
    else :
        if abs(num-guess) <= 10:
            print("Warm")
        else:
            print("Cold")
        
        