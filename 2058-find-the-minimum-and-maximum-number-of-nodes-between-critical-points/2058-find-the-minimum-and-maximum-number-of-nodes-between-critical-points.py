# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # minimum distance
        min_dist = float('inf')
        # previous node
        previous = head
        # current node
        current = head.next
        # index of the current node
        current_index = 1
        # index of the previous critical point for minimum distance
        previous_critical = 0
        # index of the first critical point for maximum distance
        first_critical = 0
        
        while current.next is not None:
            # check if the current node is a critical point
            if (previous.val > current.val and current.val < current.next.val) or (previous.val < current.val and current.val > current.next.val):
                # it current node is the first critical point found
                if previous_critical == 0:
                    previous_critical = current_index
                    first_critical = current_index
                else:
                    min_dist = min(min_dist, current_index - previous_critical)
                    previous_critical = current_index
            # advance pointers
            current_index += 1
            previous = current
            current = current.next
        # at least two critical points found
        if min_dist != float('inf'):
            return [min_dist, previous_critical - first_critical]
        
        return [-1, -1]