class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # integer -> counting sort
        
        # frequency map
        freq = {}
        # find the max and min values
        minimum, maximum = min(nums), max(nums)
        
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            
        # place each element in correct position
        i = 0
        for n in range(minimum, maximum + 1):
            while freq.get(n, 0) > 0:
                # put the element at position i
                nums[i] = n
                # increment the current index
                i += 1
                # decrement the frequency
                freq[n] -= 1
        
        return nums