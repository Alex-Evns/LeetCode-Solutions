import unittest

from Easy.ispallindrome import Solution


class TestIsPalindrome(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_single_digit_numbers_are_palindromes(self) -> None:
        self.assertTrue(self.solution.isPalindrome(0))
        self.assertTrue(self.solution.isPalindrome(7))

    def test_simple_palindromes(self) -> None:
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertTrue(self.solution.isPalindrome(12321))

    def test_non_palindromes(self) -> None:
        self.assertFalse(self.solution.isPalindrome(10))
        self.assertFalse(self.solution.isPalindrome(123))
        self.assertFalse(self.solution.isPalindrome(100002))

    def test_negative_numbers_are_not_palindromes(self) -> None:
        self.assertFalse(self.solution.isPalindrome(-121))
        self.assertFalse(self.solution.isPalindrome(-1))

    def test_large_numbers(self) -> None:
        self.assertTrue(self.solution.isPalindrome(1000000001))
        self.assertFalse(self.solution.isPalindrome(1000000002))


if __name__ == "__main__":
    unittest.main(verbosity=2)
