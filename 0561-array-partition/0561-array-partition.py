class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=False)
        result = 0
        for i in range(len(nums)):
            if i % 2:
                continue
            result += nums[i]
        return result
        