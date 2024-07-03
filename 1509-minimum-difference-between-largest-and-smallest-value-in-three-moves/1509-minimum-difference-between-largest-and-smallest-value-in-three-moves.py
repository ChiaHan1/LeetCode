class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # number of elements in nums
        n = len(nums)
        # if n is less than or equal to num the minimum difference must be 0
        if n <= 4:
            return 0
        
        # sort the array
        nums.sort()
        
        # 4 possible scenarios:
        # 1. remove 3 largest
        # 2. remove 2 largest and 1 smallest
        # 3. remove 1 largest and 2 smallest
        # 4. remove 3 smallest
        return min(
            nums[-4] - nums[0],
            nums[-3] - nums[1],
            nums[-2] - nums[2],
            nums[-1] - nums[3]
        )