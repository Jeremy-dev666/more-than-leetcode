class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fs = [0] * 128
        ft = [0] * 128
        for i in range(len(s)):
            fs[ord(s[i])] += 1
            ft[ord(t[i])] += 1
        for i in range (128):
            if fs[i] != ft[i]:
                return False
        return True
