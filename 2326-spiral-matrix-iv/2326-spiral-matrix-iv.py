# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # initialize the matrix with all -1s
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # x and y coordinate starting from top left (0, 0)
        x, y = 0, 0
        # offset for the edges
        offset = 0
        
        while head:
            matrix[y][x] = head.val
            
            # go right
            if y == offset and x < n - 1 - offset:
                x += 1
            # go down
            elif x == n - 1 - offset and y < m - 1 - offset:
                y += 1
            # go left
            elif y == m - 1 - offset and x > offset:
                x -= 1
            # go up
            else:
                y -= 1
                if y == offset + 1:
                    offset += 1
            # go to the next number
            head = head.next
            
        return matrix