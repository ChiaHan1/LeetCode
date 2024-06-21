class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]

        for i in range(1, numRows):
            # previous row
            previous = pascal[-1]
            # current row
            current = [1]
            for j in range(1, i):
                current.append(previous[j - 1] + previous[j])
            # the last 1
            current.append(1)
            pascal.append(current)
        
        return pascal