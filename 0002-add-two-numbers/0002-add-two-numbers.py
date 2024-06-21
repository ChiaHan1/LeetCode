# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        start = ListNode()
        current = start
        while (l1 != None or l2 != None):
            current.next = ListNode()
            current = current.next
            if l1 == None:
                result = l2.val + carry
                carry = result // 10
                current.val = result % 10
                l2 = l2.next
            elif l2 == None:
                result = l1.val + carry
                carry = result // 10
                current.val = result % 10
                l1 = l1.next
            else:
                result = l1.val + l2.val + carry
                carry = result // 10
                current.val = result % 10
                l1 = l1.next
                l2 = l2.next
        
        if carry == 1:
            current.next = ListNode()
            current.next.val = carry
        else:
            current.next = None
        
        return start.next
