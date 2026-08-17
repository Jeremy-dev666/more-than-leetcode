# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.q = deque()
        # 单独遍历一遍二叉树，把所有不满的节点都放入到队列q中
        bfs = deque([root])
        while bfs:
            node = bfs.popleft()
            if node.left: bfs.append(node.left)
            if node.right: bfs.append(node.right)
            if not node.left or not node.right:
                self.q.append(node)

    def insert(self, val: int) -> int:
        """遍历未满父节点列表，如果左边子节点为空就放左子，否则就放右子"""
        node = TreeNode(val)
        prnt = self.q[0]
        if not prnt.left:
            prnt.left = node
        else:
            prnt.right = node
            self.q.popleft() # 添加后当前父节点就是满的，要弹出未满父节点列表
        self.q.append(node)  # 新插入节点也要加入未满父节点列表
        return prnt.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()