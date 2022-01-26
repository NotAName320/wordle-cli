import argparse

import colors
import pyperclip

from get_word import get_word, date_diff, word_list, word_allowed
from legal_words import legal_words


if __name__ == '__main__':
    tile_correct, tile_present, tile_absent = '🟩', '🟨', '⬛'
    today_word = get_word()

    guesses_left = 6
    copy_string = ''
    letters_correct = []
    letters_present = []
    while True:
        keyboard = ''
        for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if let.lower() in letters_correct:
                keyboard += colors.color(let, bg="green")
            elif let.lower() in letters_present:
                keyboard += colors.color(let, bg="yellow")
            else:
                keyboard += let
        print(keyboard)
        while True:
            guess = input(f'Enter a guess ({guesses_left} tries left): ').lower()
            if guess.isalpha() and len(guess) == 5 and word_allowed(guess):
                break
            print('Invalid guess.')
        guesses_left -= 1

        round_results = ''
        round_results_emoji = ''
        for i in range(5):
            if guess[i] == today_word[i]:
                if guess[i] not in letters_correct:
                    letters_correct.append(guess[i])
                round_results += colors.color(guess[i].upper(), bg="green")
                round_results_emoji += tile_correct
            elif guess[i] in today_word:
                if guess[i] not in letters_present:
                    letters_present.append(guess[i])
                round_results += colors.color(guess[i].upper(), bg="yellow")
                round_results_emoji += tile_present
            else:
                round_results += guess[i].upper()
                round_results_emoji += tile_absent
        copy_string += round_results_emoji + '\n'
        print(round_results)

        if guess == today_word:
            pyperclip.copy(f'Wordle {date_diff()} {6-guesses_left}/6\n\n{copy_string}')
            print(f'Correct! The word was {today_word.upper()}.\nResults copied to clipboard!')
            break
