import datetime

from .wordlist import word_list


def date_diff():
    wordle_start = datetime.date(2021, 6, 19)
    today = datetime.date.today()
    return (today - wordle_start).days


def get_word():
    return word_list[date_diff() % len(word_list)]


if __name__ == "__main__":
    print(get_word())
