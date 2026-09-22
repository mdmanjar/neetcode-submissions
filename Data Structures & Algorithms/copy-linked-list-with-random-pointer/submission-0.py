"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:return head

        temp=head

        while temp:
            next=temp.next
            temp.next=Node(temp.val,next)
            temp=temp.next.next

        temp=head

        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        l=Node(-1)
        h=l
        while head:
            next=head.next.next
            h.next=head.next
            head.next=next
            head=next
            h=h.next
        h.next=None
        return l.next
        