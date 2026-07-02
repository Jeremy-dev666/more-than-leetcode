from collections import defaultdict

class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_node = defaultdict(ListNode)
        self.min_freq = 1

        def new_list() -> ListNode:
            dummy = ListNode(-1, -1)
            dummy.prev = dummy
            dummy.next = dummy
            return dummy
        self.freq_dummy = defaultdict(new_list)

    def get(self, key: int) -> int:
        node = self._getNode(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        # 1.取出要更新的节点（可能为None）
        node = self._getNode(key)
        if node:
            node.val = value
            return

        # 2.节点不存在就要新增插入，那么第一步要判断容量
        # 容量满了删除最不常使用的节点（且最近没被使用）
        if len(self.key_node) == self.capacity:
            dummy = self.freq_dummy[self.min_freq]
            tail_node = dummy.prev
            del self.key_node[tail_node.key]
            self._remove(tail_node)
            if dummy.prev == dummy:
                del self.freq_dummy[self.min_freq]

        new_node = ListNode(key, value)
        self.key_node[key] = new_node
        self._addFirst(self.freq_dummy[1], new_node)
        self.min_freq = 1    # 这个细节很重要

    def _getNode(self, key):
        # 1.判断node是否存在
        if key not in self.key_node:
            return None

        # 2.拿到查询的node并从链表中抽取出来
        cur_node = self.key_node[key]
        self._remove(cur_node)

        # 3.拿到node所对应的dummy节点
        dummy = self.freq_dummy[cur_node.freq]
        if dummy.prev == dummy:    # 链表为空，说明当前节点被抽出来后没有其他节点了
            del self.freq_dummy[cur_node.freq]
            # 判断这条删掉的链表是否是最左侧（最小频次的链表）是，则最小频次需要 +1
            if self.min_freq == cur_node.freq:
                self.min_freq += 1
        
        # 4.操作过的节点频次 +1
        cur_node.freq += 1

        # 5.插入到增加后的频次链表的头节点（表示最近被使用）
        self._addFirst(self.freq_dummy[cur_node.freq], cur_node)
        return cur_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addFirst(self, dummy, cur_node):
        cur_node.prev = dummy
        cur_node.next = dummy.next
        dummy.next.prev = cur_node
        dummy.next = cur_node
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)