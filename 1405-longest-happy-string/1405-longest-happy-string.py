class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # 建立大根堆
        pq = []
        if a > 0:
            heapq.heappush_max(pq, (a, "a"))
        if b > 0:
            heapq.heappush_max(pq, (b, "b"))
        if c > 0:
            heapq.heappush_max(pq, (c, "c"))

        ans = []
        while pq:
            freq, c = heapq.heappop_max(pq)

            # 字母连续重复到达2次需要换字母
            if len(ans) >= 2 and ans[-1] == c and ans[-2] == c:
                if not pq: 
                    break

                nxt_freq, nxt_c = heapq.heappop_max(pq)
                ans.append(nxt_c)
                nxt_freq -= 1
                if nxt_freq > 0:
                    heapq.heappush_max(pq, (nxt_freq, nxt_c))
                heapq.heappush_max(pq, (freq, c))

            else:
                freq -= 1
                ans.append(c)
                if freq > 0:
                    heapq.heappush_max(pq, (freq, c))

        return "".join(ans)
                    
                
