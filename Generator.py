from Alphabet import Letter, Alphabet
from random import *
import csv


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


def get_feedback(name, name_positions, probability_matrix, alphabet):
    feedback_type = input(
        "Will you evaluate the name character by character? (y/n) ")

    if feedback_type.strip().lower() == "y":
        for i in range(len(name) - 1):
            letter1 = name[i]
            letter2 = name[i + 1]
            feedback = input(
                "Was the sequence '" + letter1 + letter2 + "' good? (y/n) ")
            if feedback.strip().lower() == "y":
                print("Let's go!")
                probability_matrix[name_positions[i]
                                   ][name_positions[i + 1]] *= 1.01
            else:
                print("Will try to avoid it from now on :(")
                probability_matrix[name_positions[i]
                                   ][name_positions[i + 1]] *= 0.99
    else:
        feedback = input("Was the name '" + name + "'a good name? (y/n) ")
        if feedback.strip().lower() == "y":
            print("Awesome!")
            for i in range(len(name) - 1):
                probability_matrix[name_positions[i]
                                   ][name_positions[i + 1]] *= 1.01
        else:
            print("Dang it :(")
            for i in range(len(name) - 1):
                probability_matrix[name_positions[i]
                                   ][name_positions[i + 1]] *= 0.99

    # Normalize the probability matrix
    for i in range(26):
        total = 0
        for j in range(26):
            total += probability_matrix[i][j]
        for j in range(26):
            probability_matrix[i][j] /= total
    # Write probability matrix to file. This file will be read by the name generator.
    file_name = "output.csv"
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(0, len(alphabet)):
            writer.writerow(probability_matrix[i])


class Generator:

    def __init__(self, alphabet, probability_matrix_file):
        self.alphabet = alphabet
        self.probability_matrix = []
        with open(probability_matrix_file, newline='') as f:
            reader = csv.reader(f, delimiter=",", quotechar="|")
            self.probability_matrix = [
                [float(num) for num in row] for row in reader]

        # Normalize the probability matrix
        for i in range(26):
            total = 0
            for j in range(26):
                total += self.probability_matrix[i][j]
            for j in range(26):
                self.probability_matrix[i][j] /= total

    def generate_name(self, min_length, max_length):
        if min_length == 0:
            print("Error: names must be at least one character long")
            return

        name_length = randint(min_length, max_length)

        # Start with the first letter
        name = [self.alphabet[randint(0, len(self.alphabet) - 1)]]
        name_positions = [name[0].position]

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
            name_positions.append(previous_letter_position)

        name_string = ""
        for letter in name:
            name_string = name_string + letter.letter

        return (name_string, name_positions)

    def generate_names(self, list_length, min_name_length, max_name_length):
        names = []

        while len(names) < list_length:
            name = self.generate_name(min_name_length, max_name_length)
            names.append((name))

        print(names[0])

        feedback = input("Will you give feedback on the name(s)? (y/n) ")
        if feedback.strip().lower() == "y":
            for name in names:
                get_feedback(name[0], name[1],
                             self.probability_matrix, self.alphabet)

        return names
