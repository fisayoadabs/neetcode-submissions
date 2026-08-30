# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        # Reverse
        curr = head
        revCurr = None

        while curr:
            nextNode = curr.next
            curr.next = revCurr
            revCurr = curr
            curr = nextNode

        # Remove nth node from reversed list
        if n == 1:
            revCurr = revCurr.next
        else:
            curr = revCurr

            for _ in range(n - 2):
                curr = curr.next

            curr.next = curr.next.next

        # Reverse back
        curr = revCurr
        result = None

        while curr:
            nextNode = curr.next
            curr.next = result
            result = curr
            curr = nextNode

        return result
        