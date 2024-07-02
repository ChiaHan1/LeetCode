class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the longest streak
        longest = 0
        # make a set of nums
        numbers = set(nums)
        
        for n in numbers:
            # if n - 1 is not in the set
            if n - 1 not in numbers:
                # set current number to n
                current = n
                # current number streak
                streak = 1
                
                # if the next number is also in the set
                while current + 1 in numbers:
                    current += 1
                    streak += 1
                    
                # update the longest streak
                longest = max(longest, streak)
                
        return longest
                