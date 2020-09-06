from Generator import Generator
from Alphabet import Alphabet

al = Alphabet.english_alphabet("english")
gen = Generator(al.alphabet, "output.csv")
n = gen.generate_names(1, 4, 10)
print(n)
