# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 标记二叉树所有节点的父节点，将二叉树转换为一张无向图
        prnt_map = {}  # node : prnt
        def dfs(node, prnt):
            if node is None:
                return
            
            prnt_map[node] = prnt
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        # 从target节点开始进行图遍历
        q = deque([target])
        visited = {target}
        distance = 0
        while q and distance < k:
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in (node.left, node.right, prnt_map[node]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            distance += 1

        return [node.val for node in q]