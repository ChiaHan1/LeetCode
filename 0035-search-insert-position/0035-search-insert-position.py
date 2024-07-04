class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # this problem is basically binary search
        
        # left and right pointers
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            # found the target
            if nums[middle] == target:
                return middle
            # target is on the left
            if target < nums[middle]:
                right = middle - 1
            # target is on the right
            else:
                left = middle + 1
        
        # if target isnt in the list then return its position
        return left