# wordle-cli
Play the popular word game [Wordle](https://www.powerlanguage.co.uk/wordle/)
directly in the shell. Also allows for the option to play random Wordles and a historical Wordle.

Credit to [Josh Wardle](https://twitter.com/powerlanguish), the original creator of Wordle.

# A Warning
The file `wordle_cli/wordlist.py` includes every single word, in order, used for daily Wordles, including words for future Wordles. It is advised to avoid looking at this file unless you want to be spoiled.

# How to Play
*Note: compiled version coming soon*

1. Clone the repository into its own directory.
2. Install the dependencies in requirements.txt, either in a venv or in the site-packages.
3. Open a terminal and execute:
```
$ python wordle.py
```
4. A file `config.ini` will be generated. Run `python wordle.py -h` for help.
