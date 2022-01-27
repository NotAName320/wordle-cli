import argparse
import configparser
from os.path import exists

import colors
import pyperclip

from wordle_cli import date_diff, get_word, get_random_word, get_specific_word, word_allowed


if __name__ == '__main__':
    if not exists('./config.ini'):
        config = configparser.ConfigParser()
        config['Wordle'] = {
            'dark_mode': 'yes',
            'colorblind_mode': 'no',
            'copy_to_clipboard': 'yes',
            'wordle_cli_ad': 'yes'
        }
        with open('./config.ini', 'w') as config_file:
            config.write(config_file)
    else:
        config = configparser.ConfigParser()
        config.read('./config.ini')

    parser = argparse.ArgumentParser(description='Plays the popular game Wordle in the shell.')
    parser.add_argument('-r', '--random', help='Play a random Wordle. Overrides -n.', action='store_true')
    parser.add_argument('-n', '--number', type=int, help='Play the Wordle of a specific day.')
    args = parser.parse_args()

    if config['Wordle']['colorblind_mode'] == 'yes':
        ansi_correct, ansi_present = 'orange', 'blue'
        tile_correct, tile_present = '🟧', '🟦'
    else:
        ansi_correct, ansi_present = 'green', 'yellow'
        tile_correct, tile_present = '🟩', '🟨'

    if config['Wordle']['dark_mode'] == 'yes':
        tile_absent = '⬛'
    else:
        tile_absent = '⬜'

    if args.random:
        date = '???'
        today_word = get_random_word()
    elif args.number:
        if args.number > date_diff():
            raise ValueError('Cannot play Wordles from the future')
        date = args.number
        today_word = get_specific_word(args.number)
    else:
        date = date_diff()
        today_word = get_word()

    guesses_left = 6
    copy_string = ''
    letters_correct, letters_present, letters_wrong = [], [], []

    while True:
        keyboard = ''
        for let in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if let.lower() in letters_correct:
                keyboard += colors.color(let, bg=ansi_correct)
            elif let.lower() in letters_present:
                keyboard += colors.color(let, bg=ansi_present)
            elif let.lower() in letters_wrong:
                keyboard += colors.color(let, style="faint")
            else:
                keyboard += let
        print(keyboard)

        while True:
            guess = input(f'Enter a guess ({guesses_left} tries left): ').lower()
            if guess.isalpha() and len(guess) == 5 and word_allowed(guess):
                break
            print('Invalid guess.')
        guesses_left -= 1

        round_results, round_results_emoji = '', ''
        for i in range(5):
            if guess[i] == today_word[i]:
                if guess[i] not in letters_correct:
                    letters_correct.append(guess[i])
                round_results += colors.color(guess[i].upper(), bg=ansi_correct)
                round_results_emoji += tile_correct
            # Complicated check to ensure we only highlight yellow when there's another letter
            elif guess[i] in today_word and (guess[i] not in letters_correct or today_word.count(guess[i]) == 2):
                if guess[i] not in letters_present:
                    letters_present.append(guess[i])
                round_results += colors.color(guess[i].upper(), bg=ansi_present)
                round_results_emoji += tile_present
            else:
                if guess[i] not in letters_wrong:
                    letters_wrong.append(guess[i])
                round_results += guess[i].upper()
                round_results_emoji += tile_absent
        copy_string += round_results_emoji + '\n'
        print(round_results)

        if guess == today_word:
            print(f'Correct! The word was {today_word.upper()}.')
            copy_to_clipboard = f'Wordle {date} {6-guesses_left}/6\n\n{copy_string}'
            break

        if guesses_left == 0:
            print(f'The word was {today_word.upper()}.')
            copy_to_clipboard = (f'Wordle {date} X/6\n\n{copy_string}')
            break
    if config['Wordle']['copy_to_clipboard'] == 'yes':
        if config['Wordle']['wordle_cli_ad'] == 'yes':
            copy_to_clipboard += '\n\nPlayed in the terminal using wordle-cli\nhttps://github.com/NotAName320/wordle-cli'
        pyperclip.copy(copy_to_clipboard)
        print('Results copied to clipboard!')
