# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        # double ended queue for bfs
        queue = deque([root])
        
        while queue:
            # number of nodes in current level
            count = len(queue)
            # sum of nodes in current leve
            total = 0
            # to count if all the nodes of current level has been gone through
            current = 0
            while current < count:
                # pop a node from the queue
                node = queue.popleft()
                # add the value of the node
                total += node.val
                
                # add the children of the node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # increment the count
                current += 1
            result.append(total / count)
            
        return result
        
        
        