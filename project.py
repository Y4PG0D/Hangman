#hangman game
import random
from Hangman.Helper_Functions import create_wordlist, HANGMANPICS

while True:  # game restart loop

    #intitialize wordlist from https://github.com/Xethron/Hangman/blob/master/words.txt
    wordlist = create_wordlist()

    chosen_word = random.choice(wordlist)
    word_length = len(chosen_word)
    empty_word = ["_"] * word_length

    letters = list(chosen_word)

    guesses = 0
    wrong_guesses = []
    if word_length <= 7:
        max_guesses = 7
    else:
        max_guesses = word_length

    print(f"Hello! Welcome to Hangman. Your task is to guess the chosen word. But be careful, you only have {max_guesses} guess(es). Good Luck!")
    print(f"Your word looks like this: {empty_word} There are {len(empty_word)} letters to guess!")

    ready = input("Type 'ready' when you want to start, or anything else to quit: ")
    if ready.lower() == str("ready"):

        while guesses < max_guesses and empty_word != letters:

            guess = input("Guess a letter: ")

            if guess in letters:
                positions = [i for i, x in enumerate(letters) if x == guess]
                for pos in positions:
                    empty_word[pos] = guess
                print(f"Well Done! You have guessed a correct letter!")
                print(f"Your word looks like this: {empty_word}")
                guesses += 1
                print(f"You have {7 - guesses} guess(es) remaining. Wrong guess(es) = {wrong_guesses}")

            else:
                print("Oh no, that letter was not part of the word :(")
                print(HANGMANPICS[guesses])
                guesses += 1
                wrong_guesses.append(guess)
                print(f"Your word looks like this: {empty_word}")
                print(f"You have {7 - guesses} guess(es) remaining. Wrong guess(es) = {wrong_guesses}")

    if empty_word == letters:
        print("Congrats! You guessed the word correctly!")
    else:
        print("You lose! The word was:", chosen_word)

    # ask to play again
    play_again = input("Type 'again' to play again, or anything else to quit: ")
    if play_again.lower() != "again":
        print("Thanks for playing!")
        break











