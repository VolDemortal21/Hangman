from os import error
import random

hangman_stages = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

gameover = """  
  ██████╗  █████╗ ███╗   ███╗███████╗
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
 ██║  ███╗███████║██╔████╔██║█████╗  
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝

        ██████╗ ██╗   ██╗███████╗██████╗ 
       ██╔═══██╗██║   ██║██╔════╝██╔══██╗
       ██║   ██║██║   ██║█████╗  ██████╔╝
       ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
       ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
        ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
        
    Better luck next time ig lol"""

listofwords = [
    "apple",
    "pencil",
    "chair",
    "cat",
    "elephant",
    "cargo",
    "house",
    "sigma",
    "black",
    "white",
    "among",
    "incident",
]

found_letters = []

def wrong_amount(amount):
    if amount == 0:
        print(hangman_stages[0])
    elif amount == 1:
        print(hangman_stages[1])
    elif amount == 2:
        print(hangman_stages[2])
    elif amount == 3:
        print(hangman_stages[3])
    elif amount == 4:
        print(hangman_stages[4])
    elif amount == 5:
        print(hangman_stages[5])
    elif amount == 6:
        print(hangman_stages[6])
    else:
        print(gameover)

def hidden_word(wordcoice, found_letters):
    display = ""

    for letter in wordcoice:
        if letter in found_letters:
            display += " " + letter
        else:
            display += " _"

    return display

print("Welcome to hangman")
print("If you answer incorrectly 7 times, you will lose")
input("Hit enter to continue...")
wordcoice = random.choice(listofwords)
print("Word has been selected")

emptyspace = wordcoice
a = 0

while True:

    wrong_amount(a)
    print(hidden_word(wordcoice, found_letters))
    letter = input("Enter a letter: ").lower()

    if letter in wordcoice:
        print("Correct letter!")
        found_letters.append(letter)
    else:
        a += 1
        print("\nWrong lmao")
        
    if all(letter in found_letters for letter in wordcoice):
        print(f"\nWord was{hidden_word(wordcoice, found_letters)}")
        print("Congratulations!")
        break
    if a == 6:
        print(gameover)
        break