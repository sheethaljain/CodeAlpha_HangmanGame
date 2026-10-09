import random

# List of 5 predefined words
words = ["python", "computer", "program", "developer", "science"]

# Select a random word
secret_word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")
print("Guess the hidden word one letter at a time!")
print("You have 6 incorrect guesses available.\n")

# Main game loop
while incorrect_guesses < max_incorrect_guesses:

    # Display the current word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    # Check whether the player won
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Display remaining attempts
    print("Incorrect guesses:", incorrect_guesses, "/", max_incorrect_guesses)

    # Get the player's guess
    guess = input("Enter one letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic letter.\n")
        continue

    # Check for repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter. Try another.\n")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        incorrect_guesses += 1
        print("Wrong guess!\n")

else:
    print("You lost! The word was:", secret_word)

print("\nThanks for playing Hangman!")