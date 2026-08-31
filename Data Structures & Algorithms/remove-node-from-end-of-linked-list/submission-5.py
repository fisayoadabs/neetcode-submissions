# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        curr = head
        revCurr = None
        while curr:
            nextNode = curr.next
            curr.next = revCurr
            revCurr = curr
            curr = nextNode
        if n == 1:
            revCurr = revCurr.next
        else:
            count = 0
            curr = revCurr

            for _ in range(n - 2):
                curr = curr.next

            curr.next = curr.next.next
        newCurr = revCurr
        revvCurr = None
        while newCurr:
            nextNode = newCurr.next
            newCurr.next = revvCurr
            revvCurr = newCurr
            newCurr = nextNode
        return revvCurr
        