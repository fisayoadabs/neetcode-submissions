class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1 

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        count = 0
        while curr.next:
            if count == index-1:
                curr.next = curr.next.next
                return True
            curr = curr.next
            count += 1 
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
        
