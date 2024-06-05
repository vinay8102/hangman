import random

# List of words to choose from
words = ['python', 'hangman', 'challenge', 'programming', 'developer', 'computer', 'game', 'random', 'function']

def choose_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses. Good luck!")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "incorrect guesses left.")

        if set(word) == guessed_letters:
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nSorry, you ran out of guesses. The word was:", word)

if __name__ == "__main__":
    hangman()
