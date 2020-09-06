from Alphabet import Letter, Alphabet
from random import *


def pick_letter(i, probability_matrix, alphabet):
    r = random()
    total = 0
    for j in range(0, len(alphabet)):
        total += probability_matrix[i][j]
        if(r <= total or j == len(alphabet) - 1):
            return alphabet[j]

    print("Error")
    return alphabet[25]


def get_random_letter(alphabet, vowel_needed, probability_matrix, previous_position):

    letter = pick_letter(previous_position, probability_matrix, alphabet)

    # special case for Y, we don't care what is needed, always just put it in.
    while vowel_needed and not letter.is_vowel and letter.letter != "y":
        letter = pick_letter(previous_position, probability_matrix, alphabet)

    return letter


class Generator:

    def __init__(self, alphabet, probability_matrix):
        self.alphabet = alphabet
        self.probability_matrix = probability_matrix

    def generate_name(self, min_length, max_length):
        if min_length == 0:
            print("Error: names must be at least one character long")
            return

        name_length = randint(min_length, max_length)

        # Start with the first letter
        name = [self.alphabet[randint(0, len(self.alphabet) - 1)]]

        vowel_needed = False
        previous_letter_position = name[0].position

        while len(name) < name_length:
            # if the current letter and previous letter are consonants, we need a vowel
            if len(name) > 1:
                vowel_needed = not name[len(
                    name) - 1].is_vowel and not name[len(
                        name) - 2].is_vowel

            letter = get_random_letter(
                self.alphabet, vowel_needed, self.probability_matrix, previous_letter_position)
            name.append(letter)
            previous_letter_position = letter.position

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
