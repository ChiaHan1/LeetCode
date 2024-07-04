# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # the first node in the linked list is guaranteed to be 0
        head = head.next
        # current node pointer to iterate through the linked list
        current = head
        # pointer to the position to write to
        position = head
        
        # iterate through the linked list
        while current is not None:
            value = 0
            # sum up all the consecutive nonzero nodes
            while current.val != 0:
                value += current.val
                current = current.next
            # write the sum to the node
            position.val = value
            # advance the current pointer
            current = current.next
            # move the next node to write to to current
            position.next = current
            # advance the node to write to
            position = position.next
        return head