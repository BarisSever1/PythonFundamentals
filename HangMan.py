import random

hangman_list = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

cman = []


class Hangman:
    def __init__(self):
        self.left = 0
        self.hangman_list_ct = 0

    def word_list(self, word: str) -> list:
        wordlist = []
        for i in word:
            wordlist.append("_")
        return wordlist

    def print_current(self, wordlist: list):
        for i in range(len(wordlist) - 1):
            print(wordlist[i], end=' ')
        print(wordlist[-1])

    def guess_letter(self, letter: str, word: str, wordlist: list):
        if letter not in wordlist:
            flag = 0
            for i in range(len(word)):
                if word[i] == letter:
                    wordlist[i] = letter
                    flag = 1
            if flag == 0:
                cman.append(hangman_list[self.hangman_list_ct])
                self.hangman_list_ct += 1
        else:
            print("You have already guessed it!")

    def current_hangman(self, cman: list):
        for i in cman:
            print(i)


def main():
    word = input("Enter a guess word: ").strip().lower()
    hangman = Hangman()
    wordlist = hangman.word_list(word)
    hangman.print_current(wordlist)
    while True:
        try:
            letter = input("\nEnter a letter: ").strip().lower()
            hangman.guess_letter(letter, word, wordlist)
            hangman.print_current(wordlist)
            hangman.current_hangman(cman)
            if wordlist == list(word):
                print("You have won")
                break
        except IndexError:
            print("YOU HAVE LOST :(")
            break


main()