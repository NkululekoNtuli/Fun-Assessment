import unittest
from fun import*

class TestFun(unittest.TestCase):
    def test_dog_years(self):
        self.assertEqual(dog_years(15), "The dog's age in dog years is 73")
    
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz (15) => 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ")
        self.assertEqual(fizzbuzz(3), "Fizz (3) => 1 2 Fizz ")
        self.assertEqual(fizzbuzz(5), "Buzz (5) => 1 2 Fizz 4 Buzz ")

    def test_word_lengths(self):
        self.assertEqual(word_lengths("Yankho Chantel Maria Saliji Sponge Bob Big Mom is amazing"), 
            {'Yankho': 6, 'Chantel': 7, 'Maria': 5, 'Saliji': 6, 'Sponge': 6, 'Bob': 3, 'Big': 3, 'Mom': 3, 'is': 2, 'amazing': 7})
        
    def test_cube_sum(self):
        self.assertEqual(cube_sum(123), 36) 
        
if __name__ == "__main__":
    unittest.main()