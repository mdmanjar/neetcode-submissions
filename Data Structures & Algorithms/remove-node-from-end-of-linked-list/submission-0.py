# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(head):
            prev=None

            while head:
                next=head.next
                head.next=prev
                prev=head
                head=next
            return prev
        
        head=reverse(head)
        if n==1:return reverse(head.next)
        temp=head

        while n>2:
            n-=1
            temp=temp.next
        if temp.next:
            temp.next=temp.next.next
        return reverse(head)

        