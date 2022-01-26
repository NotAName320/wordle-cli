import pyperclip

from get_word import get_word, date_diff


if __name__ == '__main__':
    tile_correct, tile_present, tile_absent = '🟩', '🟨', '⬛'
    today_word = get_word()

    guesses_left = 6
    copy_string = ''
    while True:
        while True:
            guess = input(f'Enter a guess ({guesses_left} tries left): ').lower()
            if guess.isalpha() and len(guess) == 5:
                break
            print('Invalid guess.')
        guesses_left -= 1

        if guess == today_word:
            copy_string += tile_correct*6
            pyperclip.copy(f'Wordle {date_diff()} {6-guesses_left}/6\n\n{copy_string}')
            print(f'{tile_correct*6}\nCorrect! The word was {today_word.upper()}.\nResults copied to clipboard!')
            break


