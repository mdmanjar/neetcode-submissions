class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def mid(head):
            slow = fast = head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head):
            prev = None

            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        last = reverse(mid(head))

        while last:
            if head.val != last.val:
                return False
            last = last.next
            head = head.next

        return True