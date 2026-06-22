class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArr = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key: int) -> None:
        idx = self._hash(key)
        self.bucketArr[idx].insert(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.bucketArr[idx].delete(key)

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        return self.bucketArr[idx].exists(key)

class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def insert(self, val):
        if not self.exists(val):
            newNode = Node(val, self.head.next)
            self.head.next = newNode
    
    def delete(self, val):
        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.val == val:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def exists(self, val):
        cur = self.head.next
        while cur is not None:
            if cur.val == val:
                return True
            cur = cur.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)