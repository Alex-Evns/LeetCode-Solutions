class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {} # * Creating dictionary to store numbers and their indices

        for i, num in enumerate(nums): # * Loop through nums, create lookup of values,
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
            
        return [] # * Return empty list if no valid pair is found in lookup 