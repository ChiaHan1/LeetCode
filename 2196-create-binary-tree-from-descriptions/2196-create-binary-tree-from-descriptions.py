# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # a dict of all nodes indexed by values
        nodes = {}
        # a set of child values
        children = set()
        
        for parent, child, left in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if left:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
            
            children.add(child)
        
        # iterate through every noe
        for n in nodes:
            # if n is not a child of any other node
            if n not in children:
                # found the root
                return nodes[n]