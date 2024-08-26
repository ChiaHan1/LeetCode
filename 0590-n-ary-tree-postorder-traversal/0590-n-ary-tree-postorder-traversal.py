"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        if root is None:
            return result
        
        # stack for tracersal
        node_stack = [root]
        # temporarily hold the nodes in reverse order before added
        reverse_stack = []
        
        while node_stack:
            current = node_stack.pop()
            reverse_stack.append(current)
            
            # push all the children of the current node to node_stack
            for c in current.children:
                node_stack.append(c)
                
        while reverse_stack:
            result.append(reverse_stack.pop().val)
        
        return result