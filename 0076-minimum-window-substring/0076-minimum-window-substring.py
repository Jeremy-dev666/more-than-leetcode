class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if n > m:
            return ""
        ft = Counter(t)
        fs = Counter()
        l = r = 0
        valid = 0
        ans = float('inf')
        start = end = -1
        while r < m:
            if s[r] in ft:
                fs[s[r]] += 1
                if fs[s[r]] == ft[s[r]]:
                    valid += 1
            while valid == len(ft):
                if r - l + 1 < ans:
                    start = l
                    end = r
                    ans = r - l + 1
                if s[l] in ft:
                    fs[s[l]] -= 1
                    if fs[s[l]] < ft[s[l]]:
                        valid -= 1
                l += 1
            r += 1
        return "" if ans == float('inf') else s[start:end+1]
        