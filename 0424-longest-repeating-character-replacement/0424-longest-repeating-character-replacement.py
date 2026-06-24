from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = defaultdict(int)
        max_f = 0
        l = r = 0
        while r < len(s):
            f[s[r]] += 1
            max_f = max(max_f, f[s[r]])
            if r - l + 1 - max_f > k:
                f[s[l]] -= 1
                l += 1
            ans = r - l + 1
            r += 1
        return ans