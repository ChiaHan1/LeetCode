class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 1. a XOR a = 0
        # 2. 0 XOR a = a
        # ---------------------
        # | 4 | 1 | 2 | 1 | 2 |
        # ---------------------
        #   4 XOR 1 XOR 2 XOR 1 XOR 2
        # = 4 XOR (1 XOR 1) XOR (2 XOR 2)
        # = 4 XOR 0 XOR 0
        # = 4 XOR 0
        # = 4

        unique = nums[0]
        for i in range(1, len(nums)):
            unique ^= nums[i]
        return unique            