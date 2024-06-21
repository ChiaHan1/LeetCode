class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority = None
        majority_count = 0
        
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
            if counts[n] > majority_count:
                majority_count = counts[n]
                majority = n
        
        return majority