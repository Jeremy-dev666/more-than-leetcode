import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)
        for f in freq.values():
            if f > (n + 1) // 2:
                return ""

        mx_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(mx_heap)

        ans = []
        prev_cnt, prev_char = 0, ""
        while mx_heap:
            cnt, char = heapq.heappop(mx_heap)
            ans.append(char)
            if prev_cnt < 0:
                heapq.heappush(mx_heap, (prev_cnt, prev_char))
            prev_cnt, prev_char = cnt + 1, char

        return "".join(ans)