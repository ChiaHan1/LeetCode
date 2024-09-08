# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None] * k
        
        # count the number of nodes in the linked list
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        
        # minimum number of nodes in each part
        size = count // k
        # remaining nodes
        rest = count % k
        
        current = head
        prev = current
        # for each part
        for i in range(k):
            # the head of this part
            part_head = current
            # calculate the number of nodes in this part
            current_size = size
            if rest > 0:
                current_size += 1
                rest -= 1
            # traverse to the end of this part
            for j in range(current_size):
                prev = current
                if current is not None:
                    current = current.next
            # cut of the rest of linked list
            if prev is not None:
                prev.next = None
            result [i] = part_head
        return result