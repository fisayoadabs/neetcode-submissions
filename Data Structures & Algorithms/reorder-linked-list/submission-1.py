# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        while curr.next and curr.next.next:
            lastNode = curr
            while lastNode.next.next:
                lastNode = lastNode.next
            movingNode = lastNode.next
            movingNode.next = curr.next
            lastNode.next = None
            curr.next = movingNode
            curr = movingNode.next

        