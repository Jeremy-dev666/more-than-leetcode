import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # 频次超过一半一定无解
        # 每次贪心的先放频次最高的
        # 取出来用了的，下一步不能用（延迟放置）

        freq = Counter(s)
        n = len(s)
        for cnt in freq.values():
            if cnt > (n + 1) // 2:
                return ""
        
        max_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(max_heap)

        ans = []
        prev_cnt, prev_char = 0, ""
        while max_heap:
            cnt, char = heapq.heappop(max_heap)
            ans.append(char)
            if prev_cnt < 0:
                heapq.heappush(max_heap, (prev_cnt, prev_char))
            
            prev_cnt, prev_char = cnt+1, char
        
        return "".join(ans)
        
