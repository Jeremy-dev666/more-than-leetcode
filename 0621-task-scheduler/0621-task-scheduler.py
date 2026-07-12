from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1.找出最高频率
        freq = Counter(tasks).values()
        maxv = max(freq)

        # 2.统计最高频标签数量
        maxv_freq = sum(f == maxv for f in freq)

        # gaps = maxv - 1
        # len(gap) = n + 1
        # tail = maxv_freq
        return max(len(tasks), (n + 1) * (maxv - 1) + maxv_freq)