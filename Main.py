from Generator import Generator
from Alphabet import Alphabet

al = Alphabet.english_alphabet()
gen = Generator(al.alphabet)
n = gen.generate_names(4, 4, 4)
print(n)
