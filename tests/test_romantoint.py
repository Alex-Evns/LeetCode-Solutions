import unittest

from Easy.romantoint import Solution


class TestRomanToInt(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_single_character_values(self) -> None:
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("V"), 5)
        self.assertEqual(self.solution.romanToInt("X"), 10)
        self.assertEqual(self.solution.romanToInt("L"), 50)
        self.assertEqual(self.solution.romanToInt("C"), 100)
        self.assertEqual(self.solution.romanToInt("D"), 500)
        self.assertEqual(self.solution.romanToInt("M"), 1000)

    def test_simple_additive_cases(self) -> None:
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("XXVII"), 27)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_subtractive_cases(self) -> None:
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("XL"), 40)
        self.assertEqual(self.solution.romanToInt("XC"), 90)
        self.assertEqual(self.solution.romanToInt("CD"), 400)
        self.assertEqual(self.solution.romanToInt("CM"), 900)

    def test_mixed_complex_cases(self) -> None:
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.solution.romanToInt("MMXXIV"), 2024)
        self.assertEqual(self.solution.romanToInt("MDCLXVI"), 1666)


if __name__ == "__main__":
    unittest.main(verbosity=2)
