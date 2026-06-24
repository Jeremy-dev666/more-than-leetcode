class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        f = [0] * 128
        ans = 0
        while r < n:
            idx = ord(s[r])
            f[idx] += 1
            while f[idx] > 1:
                f[ord(s[l])] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans