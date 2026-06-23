class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return self.isP(s, l, r - 1) or self.isP(s, l + 1, r)
            l += 1
            r -= 1
        return True
    
    def isP(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True