# Importing modules

import random
import time

# Greetings

print("Welcome to Hangman Game\n")
player = input("Enter your Name:")
print("Hello" + player + "Good Luck!")
time.sleep(2)
print("The Hangman Game is staring")
time.sleep(3)


# Parameter for the game

def main():
    global count, display, word, already_gussed, length, play_game
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                      "plants", "name"]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_' * length
    already_gussed = []


# Loop for play again after 1st round

def play_loop():
    global play_game
