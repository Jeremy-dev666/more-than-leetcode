class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnts = [0] * 26
        for c in tasks:
            cnts[ord(c) - ord('A')] += 1

        maxv, maxv_freq = 0, 0
        for i in range(26):
            maxv = max(maxv, cnts[i])

        for i in range(26):
            maxv_freq += 1 if maxv == cnts[i] else 0
        return max(len(tasks), (n + 1) * (maxv - 1) + maxv_freq)