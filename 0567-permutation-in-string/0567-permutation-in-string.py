class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        f = Counter(s1)
        for i, c in enumerate(s2):
            f[c] -= 1
            if f[c] == 0:
                del f[c]
            if i < n - 1:
                continue
            if len(f) == 0:
                return True
            out = s2[i - n + 1]
            f[out] += 1
            if f[out] == 0:
                del f[out]
        return False