from Alphabet import Letter, Alphabet
from random import *


def get_random_letter(alphabet, vowel_needed):

    ran = randint(0, 25)
    letter = alphabet[ran]
    print(ran)

    # special case for Y, we don't care what is needed, always just put it in.
    while vowel_needed and not letter.is_vowel and letter.letter != "y":
        letter = alphabet[randint(0, 25)]

    return letter


class Generator:

    def __init__(self, alphabet):
        self.alphabet = alphabet

    def generate_name(self, min_length, max_length):
        name_length = randint(min_length, max_length)

        name = []
        vowel_needed = False
        while len(name) < name_length:
            # if the current letter and previous letter are consonants, we need a vowel
            if len(name) > 1:
                vowel_needed = not name[len(
                    name) - 1].is_vowel and not name[len(
                        name) - 2].is_vowel

            letter = get_random_letter(self.alphabet, vowel_needed)
            name.append(letter)

        name_string = ""
        for letter in name:
            name_string = name_string + letter.letter

        return name_string

    def generate_names(self, list_length, min_name_length, max_name_length):
        names = []

        while len(names) < list_length:
            name = self.generate_name(min_name_length, max_name_length)
            names.append(name)

        return names
