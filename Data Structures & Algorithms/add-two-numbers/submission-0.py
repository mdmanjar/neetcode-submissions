# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode(-1)
        h=l
        carry=0

        while l1 or l2:
            sm=carry
            if l1:
                sm+=l1.val
                l1=l1.next
            if l2:
                sm+=l2.val
                l2=l2.next
            h.next=ListNode(sm%10)
            carry=sm//10
            h=h.next
        if carry:
            h.next=ListNode(carry)
        return l.next
        