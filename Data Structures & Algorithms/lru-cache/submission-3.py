class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = None
        self.tail = None
        self.count = 0
        

    def get(self, key: int) -> int:
        if self.count == 0:
            return -1
        curr = self.storage
        result = -1
        while curr:
            if curr.key == key:
                result = curr.val
                break
            curr = curr.next
        if curr and curr != self.storage:
            
            if curr == self.tail:
                self.tail = curr.prev
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev

            # Move curr to the front
            curr.prev = None
            curr.next = self.storage
            self.storage.prev = curr
            self.storage = curr
        return result

    def put(self, key: int, value: int) -> None:
        # Check if key already exists
        curr = self.storage

        while curr:
            if curr.key == key:
                # Update value
                curr.val = value

                # Move to front if not already there
                if curr != self.storage:
                    if curr == self.tail:
                        self.tail = curr.prev

                    curr.prev.next = curr.next

                    if curr.next:
                        curr.next.prev = curr.prev

                    curr.prev = None
                    curr.next = self.storage
                    self.storage.prev = curr
                    self.storage = curr

                return

            curr = curr.next
        head = Node(key, value)
        if self.storage is None:
            self.storage = head
            self.tail = head
            self.count += 1
            return
        if self.count == self.capacity:
            old = self.tail
            if old.prev:
                old.prev.next = None
                self.tail = old.prev
            else:
                self.storage = None
                self.tail = None
            self.count -= 1
        head.next = self.storage
        if self.storage:
            self.storage.prev = head
        self.storage = head
        if self.tail is None:
            self.tail = head
        self.count +=1

        
