class MyHashMap:

    def __init__(self):
        self.keyRange = 769
        self.bucketArr = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        if self.bucketArr[idx].exists(key):
            self.bucketArr[idx].delete(key)
        self.bucketArr[idx].insert(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.bucketArr[idx].get(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        return self.bucketArr[idx].delete(key)

class Node:
    def __init__(self, key, val, nextNode=None):
        self.key = key
        self.val = val
        self.next = nextNode

class Bucket:
    def __init__(self):
        self.head = Node(0, 0)

    def exists(self, key):
        cur = self.head.next
        while cur is not None:
            if cur.key == key:
                return True
            cur = cur.next
        return False

    def get(self, key):
        cur = self.head.next
        while cur is not None:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def insert(self, key, val):
        if not self.exists(key):
            newNode = Node(key, val, self.head.next)
            self.head.next = newNode

    def delete(self, key):
        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)