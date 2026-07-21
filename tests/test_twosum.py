import unittest

from Easy.twosum import Solution


class TestTwoSum(unittest.TestCase):
    def test_returns_expected_indices_for_multiple_cases(self) -> None:
        solution = Solution()

        cases = [
            ([2, 7, 11, 15], 9, [0, 1], "basic valid pair"),
            ([3, 2, 4], 6, [1, 2], "valid pair in the middle"),
            ([1, 2, 3, 4], 8, [], "no valid pair"),
            ([5, 5, 5], 10, [0, 1], "duplicate values"),
        ]

        for nums, target, expected, description in cases:
            with self.subTest(description=description):
                result = solution.twoSum(nums, target)
                self.assertEqual(result, expected)
                print(f"PASS: {description} -> {result}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
