import datetime
from random import choice

from .legal_words import legal_words
from .wordlist import word_list


def date_diff():
    wordle_start = datetime.date(2021, 6, 19)
    today = datetime.date.today()
    return (today - wordle_start).days


def get_word():
    return word_list[date_diff() % len(word_list)]


def get_random_word():
    return choice(word_list)


def get_specific_word(number):
    return word_list[number % len(word_list)]


def word_allowed(word):
    return word in legal_words or word in word_list


def random_word_meets_conditions(word):
    # For Absurdle
    def letter_match(template, word_to_try):
        for i in range(5):
            if template[i] == '-':
                continue
            if template[i] != word_to_try[i]:
                return False
        return True
    return choice([x for x in word_list if letter_match(word, x)])
