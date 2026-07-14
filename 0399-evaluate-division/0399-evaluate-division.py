class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [1.0] * n

    def find(self, x):
        if self.parent[x] != x:
            root = self.find(self.parent[x])
            # weight[k] 表示 儿子/爸爸
            # 那么 weight 递归下去：(儿子/爸爸) * (爸爸 / 爷爷) = 儿子/爷爷
            # 所以假设要查询a -> c，
            # 那么 a -> root = weight[a], c -> root = weight[c]
            # 所以 a -> c = a / c = (a / root) / (c / root) = weight[a] / weight[c]
            self.weight[x] *= self.weight[self.parent[x]]
            self.parent[x] = root
        return self.parent[x]

    def union(self, a, b, val):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        self.parent[rb] = ra
        # 因为以上把rb挂到了ra上，所以求的是 rb(儿子) / ra(爸爸) = ?
        # a = weight[a] * ra
        # b = weight[b] * rb
        # a / b = val  ->  a = val * b
        # weight[a] * ra = val * weight[b] * rb
        # 现在把rb挂到ra上，那么ra就是爸爸，所以
        # rb / ra = self.weight[rb] = weight[a] / (val * weight[b])
        self.weight[rb] = self.weight[a] / (self.weight[b] * val)

    def query(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            return -1.0
        # a / b = (weight[a] * ra) / (weight[b] * rb)
        # 因为 ra = rb, 所以 a / b = weight[a] / weight[b]
        return self.weight[a] / self.weight[b]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 字符串节点进行编号映射
        idx_map = {}
        # 如果这个变量名之前没出现过，就给它分配新编号。编号就是当前字典的长度
        for a, b in equations:
            if a not in idx_map:
                idx_map[a] = len(idx_map)
            if b not in idx_map:
                idx_map[b] = len(idx_map)

        # 处理成并查集
        uf = UF(len(idx_map))
        for (a, b), val in zip(equations, values):
            uf.union(idx_map[a], idx_map[b], val)

        # 查询
        ans = []
        for i, j in queries:
            if i not in idx_map or j not in idx_map:
                ans.append(-1.0)
            else:
                ans.append(uf.query(idx_map[i], idx_map[j]))

        return ans
