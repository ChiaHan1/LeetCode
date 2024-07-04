# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointer pointing to the previous node
        previous = None
        # current node
        current = head
        
        while current:
            # the original next node
            temp = current.next
            # set the next node of the current node to the original previous node
            current.next = previous
            # set the previous node to the current node for the next iteration
            previous = current
            # advance to the next node
            current = temp
        
        return previous
            
            