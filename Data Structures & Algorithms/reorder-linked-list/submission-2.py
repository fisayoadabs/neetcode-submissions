# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        revCurr = None
        curr = slow.next
        slow.next = None
        while curr:
            nextNode = curr.next
            curr.next = revCurr
            revCurr = curr
            curr = nextNode
        first = head
        second = revCurr

        while first and second:
            nextFirst = first.next
            nextSecond = second.next
            first.next = second
            second.next = nextFirst
            first = nextFirst
            second = nextSecond
        