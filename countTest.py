import unittest
from count import contador

#teste unitário
class TestStringMethods(unittest.TestCase):
    def teste01_contador_returna_disc(self):
        d = contador("o doce mais doce")
        self.assertEqual(type(d), type({"dici: "exemplo"}), "Passou no teste")
                                        
        def teste02_contador(self):
        d = contador("o doce mais doce")
        self.assertEqual(d,{"0":1 "mais":2 "doce":2})

if __name__ == "__main__"
unittest.main(verbosity.2)