# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # the output array for in order traversal
        output = []
        # stack
        stack = []
        # current node
        current = root
        
        while current or stack:
            # go to the leftmost child of current node
            while current:
                # add current node to the stack
                stack.append(current)
                # move current to the left
                current = current.left
            # pop the current leftmost child
            current = stack.pop()
            # add to the result
            output.append(current.val)
            # move current to the right
            current = current.right
        return output
            
        