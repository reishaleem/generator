class Letter:

    # letter is something like 'a' or 'A', ie just a letter.
    def __init__(self, letter, is_vowel):
        self.letter = letter
        self.is_vowel = is_vowel


class Alphabet:

    # alphabet should be a list of all the Letters in the alphabet being used. It could be the simple ABCs, or a custom alphabet.
    # Note when we say Letters, we mean something with a letter and an is_vowel value
    def __init__(self, alphabet):
        self.alphabet = alphabet

    @classmethod
    def english_alphabet(cls):
        letterList = [
            Letter("a", True),
            Letter("b", False),
            Letter("c", False),
            Letter("d", False),
            Letter("e", True),
            Letter("f", False),
            Letter("g", False),
            Letter("h", False),
            Letter("i", True),
            Letter("j", False),
            Letter("k", False),
            Letter("l", False),
            Letter("m", False),
            Letter("n", False),
            Letter("o", True),
            Letter("p", False),
            Letter("q", False),
            Letter("r", False),
            Letter("s", False),
            Letter("t", False),
            Letter("u", True),
            Letter("v", False),
            Letter("w", False),
            Letter("x", False),
            Letter("y", True),
            Letter("z", False),
        ]

        return Alphabet(letterList)
