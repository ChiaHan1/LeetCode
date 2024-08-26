# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # make a list of values node in in order traversal
        values = []
        # stack for in order traversal
        stack = []
        current = root
        
        while True:
            # go to the left most node of the current subtree
            if current is not None:
                stack.append(current)
                current = current.left
            # have reached the left most node
            elif stack:
                # pop the node with minimum value of the current subtree
                current = stack.pop()
                # append the value to the list
                values.append(current.val)
                # go to the right subtree
                current = current.right
            # done with traversing the tree
            else:
                break
                
        print(values)
        
        min_diff = float('inf')
        for i in range(len(values) - 1):
            min_diff = min(min_diff, values[i + 1] - values[i])
            
        return min_diff
    