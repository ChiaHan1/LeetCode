class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # iterate through the first n - 2 elements
        for i in range(len(arr) - 2):
            # bitwise and the next 3 numbers and if the lsb is 1 they are all odds
            if arr[i] & arr[i + 1] & arr[i + 2] & 1:
                return True
        return False
            