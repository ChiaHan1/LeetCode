class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        
        while low < high:
            n = numbers[low] + numbers[high]
            
            if n == target:
                # return + 1 since the array is 1 indexed
                return [low + 1, high + 1]
            elif n < target:
                low += 1
            else:
                high -= 1
        # if no such pair was found
        return [-1, -1]