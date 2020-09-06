from Generator import Generator
from Alphabet import Alphabet

al = Alphabet.english_alphabet("english")
# file_name = al.get_probability_matrix("english human") # only want to do this when output.csv needs to be created
gen = Generator(al.alphabet, "output.csv")
n = gen.generate_names(1, 4, 10)
print(n)
