# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Do not return anything, modify head in-place instead.

        # find the middle of linked list

        def middle(head):

            slow=head
            fast=head

            while fast and fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next

            return slow

        # reverse the linked list

        def reverse(head):

            prev=None

            while head:
                nxt=head.next
                head.next=prev
                prev=head
                head=nxt

            return prev


        back=middle(head)
        mid=reverse(back.next)
        back.next=None

        # Reorder List

        while mid:
            nxt=head.next
            nxt1=mid.next
            head.next=mid
            head=head.next
            head.next=nxt
            head=head.next
            mid=nxt1

        