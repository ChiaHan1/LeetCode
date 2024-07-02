class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # initialize the counter of the current number
        count = 1
        # pointer to the current position of the updated array
        j = 1
        
        for i in range(1, len(nums)):
            # if current number is the same as the previous number
            if nums[i - 1] == nums[i]:
                # increment the counter
                count += 1
            else:
                # reset the counter
                count = 1
            if count <= 2:
                # copy the element over
                nums[j] = nums[i]
                # update the pointer to the updated array
                j += 1
        return j