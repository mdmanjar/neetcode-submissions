# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(l1,l2):
            h=ListNode()
            l3=h

            while l1 and l2:
                if l1.val<l2.val:
                    l3.next=l1
                    l1=l1.next
                else:
                    l3.next=l2
                    l2=l2.next
                l3=l3.next
            l3.next=l1 or l2
            return h.next
        
        def divid(left,right):
            if left>right:return None
            if left==right:
                return lists[left]
            mid=left+(right-left)//2
            return merge(divid(left,mid),divid(mid+1,right))
        return divid(0,len(lists)-1)

