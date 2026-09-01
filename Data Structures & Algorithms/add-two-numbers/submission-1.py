# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Val = ""
        l2Val = ""
        l1Curr = l1
        l2Curr = l2
        while l1Curr:
            l1Val = f"{l1Curr.val}" + l1Val
            l1Curr = l1Curr.next
        while l2Curr:
            l2Val = f"{l2Curr.val}" + l2Val
            l2Curr = l2Curr.next
        answer = int(l1Val) + int(l2Val)
        result = None
        for i in f"{answer}":
            newNode = ListNode(int(i))
            newNode.next = result
            result = newNode
        return result

