class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}  # val -> TreeNode
        children = set()

        # 建树
        for p, c, is_left in descriptions:
            if p not in nodes:
                nodes[p] = TreeNode(p)
            if c not in nodes:
                nodes[c] = TreeNode(c)
            if is_left:
                nodes[p].left = nodes[c]
            else:
                nodes[p].right = nodes[c]
            children.add(c)  # c 不是根节点

        for p, node in nodes.items():
            if p not in children:  # node 是根节点
                return node
