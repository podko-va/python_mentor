def make_hangman(secret_word):
    guesses = []
    bad_guesses = 0  # неправильные попытки

    def hangman_closure(letter):
        nonlocal bad_guesses
        if letter not in guesses:
            guesses.append(letter)

        # Строим отображаемое слово
        display = ""
        for char in secret_word:
            if char in guesses:
                display += char
            else:
                display += "_"
        print("Current word:", display)

        # Проверка, угадана ли буква
        if letter not in secret_word:
            bad_guesses += 1
            print(f"Wrong guess! Total wrong guesses: {bad_guesses}")

        # Проверка победы
        if set(secret_word).issubset(set(guesses)):
            print("🎉 Congratulations! You guessed the word!")
            return True
        else:
            return False

    return hangman_closure

if __name__ == "__main__":
    secret = input("Enter the secret word: ").lower()
    play = make_hangman(secret)

    while True:
        guess = input("Guess a letter: ").lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Please enter one valid letter.")
            continue
        game_over = play(guess)
        if game_over:
            break