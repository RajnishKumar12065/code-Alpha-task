import random

def hangman():
    # 5 predefined words
    words = ["python", "coding", "hangman", "program", "computer"]
    word = random.choice(words)  # randomly select a word
    guessed_letters = []  # store correct guesses
    wrong_guesses = 0
    max_guesses = 6

    print("Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")

    # main game loop
    while wrong_guesses < max_guesses:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", display_word)

        # check if player has won
        if display_word == word:
            print("🎉 Congratulations! You guessed the word correctly:", word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("✅ Good guess!")
        else:
            wrong_guesses += 1
            print("❌ Wrong guess! Attempts left:", max_guesses - wrong_guesses)

    else:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()