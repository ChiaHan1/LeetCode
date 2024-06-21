class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # sort the array
        nums.sort()
        # the array of answers
        answer = []

        for i in range(len(nums) - 2):
            # to avoid duplicate numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # early exit
            if nums[i] > 0:
                break
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
            
                # if sum of the three numbers is < 0
                if total < 0:
                    # increment the smaller number
                    l += 1
                # if sum of the three numbers is > 0
                elif total > 0:
                    # decrement the larger number
                    r -= 1
                # a solution triplet found
                else:
                    num1 = nums[i]
                    num2 = nums[l]
                    num3 = nums[r]
                    answer.append([num1, num2, num3])

                    # skip the duplicate numbers
                    while l < r and nums[l] == num2:
                        l += 1
                    while l < r and nums[r] == num3:
                        r -= 1

        return answer