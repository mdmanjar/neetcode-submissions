# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def size(head):
            sz=0
            while head:
                sz+=1
                head=head.next
            return sz
        l1=size(headA)
        l2=size(headB)
        if l1<l2:headA,headB=headB,headA
        diff=abs(l2-l1)

        while diff>0:
            headA=headA.next
            diff-=1
        
        while headA is not None and headB is not None:

            if headA==headB:return headA
            headA=headA.next
            headB=headB.next
        return None
        