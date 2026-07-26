from collections import defaultdict, Counter

class DetectSquares:

    def __init__(self):
        self.cnt = Counter()             # cnt[(x, y)] 记录点出现次数
        self.col = defaultdict(Counter)  # col[x] 是一个 Counter，记录该列上各 y 值出现次数
 

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[(x, y)] += 1
        self.col[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        if x not in self.col:
            return 0
        # 查找第二个点：遍历横坐标为x上的所有y及对应出现的次数
        for y2, c2 in self.col[x].items():
            if y2 == y:
                continue
            d = y2 - y
            # 查找第三第四个点：
            for nx in (x + d, x - d):
                ans += c2 * self.cnt[(nx, y)] * self.cnt[(nx, y2)]

        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)