import csv


class Letter:

    # letter is something like 'a' or 'A', ie just a letter.
    # position is the number in the alphabet (so, a would be 1)
    def __init__(self, letter, is_vowel, position):
        self.letter = letter
        self.is_vowel = is_vowel
        self.position = position


def get_english_name_prob_matrix(alphabet):
    # Start all probabilites at 0
    probability = [[0 for i in range(26)] for i in range(26)]

    with open("english_names.csv", newline='') as csvfile:
        names = csv.reader(csvfile, delimiter=",", quotechar="|")
        for value in names:
            name = value[0].lower()
            for i in range(len(name) - 1):
                letter1 = name[i]
                letter2 = name[i + 1]
                first_num = 0
                second_num = 0
                # this just assigns first and second num to the position of each letter in the alphabet. See if we can simplify this later.
                for j in range(26):

                    if letter1 == alphabet[j].letter:
                        first_num = alphabet[j].position
                    if letter2 == alphabet[j].letter:
                        second_num = alphabet[j].position
                # Add one to the number of times letter number i is followed by letter number i+1.
                probability[first_num][second_num] += 1

    # Normalize the matrix
    normalized_probability = probability
    for i in range(26):
        total = 0
        for j in range(26):
            total += probability[i][j]
        if (total > 0):
            for j in range(26):
                normalized_probability[i][j] = probability[i][j]/total
        else:
            for j in range(26):
                normalized_probability[i][j] = len(alphabet)**(-1)

    return normalized_probability


class Alphabet:

    # alphabet should be a list of all the Letters in the alphabet being used. It could be the simple ABCs, or a custom alphabet.
    # Note when we say Letters, we mean something with a letter and an is_vowel value
    def __init__(self, alphabet, probability_matrix):
        self.alphabet = alphabet
        self.probability_matrix = probability_matrix

    @classmethod
    def english_alphabet(cls, names_category):
        letterList = [
            Letter("a", True, 0),
            Letter("b", False, 1),
            Letter("c", False, 2),
            Letter("d", False, 3),
            Letter("e", True, 4),
            Letter("f", False, 5),
            Letter("g", False, 6),
            Letter("h", False, 7),
            Letter("i", True, 8),
            Letter("j", False, 9),
            Letter("k", False, 10),
            Letter("l", False, 11),
            Letter("m", False, 12),
            Letter("n", False, 13),
            Letter("o", True, 14),
            Letter("p", False, 15),
            Letter("q", False, 16),
            Letter("r", False, 17),
            Letter("s", False, 18),
            Letter("t", False, 19),
            Letter("u", True, 20),
            Letter("v", False, 21),
            Letter("w", False, 22),
            Letter("x", False, 23),
            Letter("y", True, 24),
            Letter("z", False, 25),
        ]

        probability = get_english_name_prob_matrix(letterList)

        # Write probability matrix to file. This file will be read by the name generator.
        file_name = "output.csv"
        with open(file_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(0, len(letterList)):
                writer.writerow(probability[i])

        return Alphabet(letterList, probability)
