# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        twoCurr = head
        while twoCurr and twoCurr.next:
            curr = curr.next
            twoCurr = twoCurr.next.next
            if curr == twoCurr:
                return True
        return False