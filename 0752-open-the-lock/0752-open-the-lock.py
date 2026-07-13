from collections import deque

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        s = "0000"
        if s == target:
            return 0
        dead = set(deadends)
        if s in dead:
            return -1
        return self.bfs(s, target, dead)

    def bfs(self, s: str, t: str, dead: set) -> int:
        # d1 从起点 s 开始搜索（正向）
        # d2 从终点 t 开始搜索（反向）
        d1, d2 = deque([s]), deque([t])
        # m1 和 m2 分别记录两个方向上各状态经过多少次转换而来
        m1, m2 = {s: 0}, {t: 0}

        # 只有两个队列都不空，才有必要继续搜索
        # 如果其中一个队列空了，说明该方向搜到底也到不了目标
        while d1 and d2:
            if len(d1) <= len(d2):
                res = self.update(d1, m1, m2, dead)
            else:
                res = self.update(d2, m2, m1, dead)
            if res != -1:
                return res
        return -1

    def update(self, dq: deque, cur: dict, other: dict, dead: set) -> int:
        # 每次扩展一整层
        for _ in range(len(dq)):
            poll = dq.popleft()
            step = cur[poll]

            # 枚举替换哪个位置
            for i in range(4):  # 四个密码位置

                # 正转 / 反转，枚举偏移量 -1 和 +1
                for j in (-1, 1):
                    nxt = (int(poll[i]) + j) % 10  # Python 的 % 对负数结果非负，无需特判

                    # 拼接变化的第i位密码
                    new_str = poll[:i] + str(nxt) + poll[i+1:]

                    if new_str in dead:  # 死锁继续
                        continue
                    if new_str in cur:   # 当前访问过，继续
                        continue

                    # 如果在另一方向出现过，说明找到最短路
                    if new_str in other:
                        return step + 1 + other[new_str]
                        
                    dq.append(new_str)
                    cur[new_str] = step + 1
        return -1