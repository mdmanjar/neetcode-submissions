# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k==1:
            return head
        def reverse(head):
            prev=None

            while head:
                next=head.next
                head.next=prev
                prev=head
                head=next
            return prev
        
        def dfs(head):
            if head is None or head.next is None:return head
            count=k
            temp=head

            while temp and count>1:
                temp=temp.next
                count-=1
            if temp is None:return head
            next=temp.next
            temp.next=None
            temp=reverse(head)
            head.next=dfs(next)
            return temp
            
        return dfs(head)



        