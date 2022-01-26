import datetime

from legal_words import legal_words
from wordlist import word_list


def date_diff():
    wordle_start = datetime.date(2021, 6, 19)
    today = datetime.date.today()
    return (today - wordle_start).days


def get_word():
    return word_list[date_diff() % len(word_list)]


def word_allowed(word):
    return word in legal_words or word in word_list


if __name__ == "__main__":
    print(get_word())
