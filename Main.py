from Generator import Generator
from Alphabet import Alphabet

al = Alphabet.english_alphabet()
gen = Generator(al.alphabet, al.probability_matrix)
n = gen.generate_name(4, 10)
print(n)
