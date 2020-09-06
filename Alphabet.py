class Letter:

    # letter is something like 'a' or 'A', ie just a letter.
    # position is the number in the alphabet (so, a would be 1)
    def __init__(self, letter, is_vowel, position):
        self.letter = letter
        self.is_vowel = is_vowel
        self.position = position


class Alphabet:

    # alphabet should be a list of all the Letters in the alphabet being used. It could be the simple ABCs, or a custom alphabet.
    # Note when we say Letters, we mean something with a letter and an is_vowel value
    def __init__(self, alphabet, probability_matrix):
        self.alphabet = alphabet
        self.probability_matrix = probability_matrix

    @classmethod
    def english_alphabet(cls):
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

        # Start all probabilites at 1
        probability = [[1 for i in range(26)] for i in range(26)]

        # these are just for show right now. We really want the program to be able to determine these
        probability[23][23] = 0  # No xx.
        probability[12][3] = 0.1  # Rare md.
        probability[16][17] = 0  # No qr.
        probability[23][16] = 0  # No xq.
        probability[23][12] = 0  # No xm.

        # Normalize the probability matrix
        for i in range(26):
            total = 0
            for j in range(26):
                total += probability[i][j]
            for j in range(26):
                probability[i][j] /= total

        return Alphabet(letterList, probability)
