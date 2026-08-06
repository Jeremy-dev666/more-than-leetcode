# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        start_node = None

        def build_par(node, par):
            nonlocal start_node
            if not node:
                return

            parent[node.val] = par

            if start == node.val:
                start_node = node
            
            build_par(node.left, node)
            build_par(node.right, node)

        build_par(root, None)

        visited = {start}
        q = deque([start_node])
        minutes = -1
        while q:
            minutes += 1
            for _ in range(len(q)):
                cur = q.popleft()
                neighbors = [cur.left, cur.right, parent[cur.val]]
                for nei in neighbors:
                    if nei and nei.val not in visited:
                        q.append(nei)
                        visited.add(nei.val)

        return minutes