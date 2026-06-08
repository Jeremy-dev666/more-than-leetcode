class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        n = len(s)

        for i in range (n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left + 1 > end - start:
                start = left
                end = right
        
        for i in range (n - 1):
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left + 1 > end - start:
                start = left
                end = right

        return s[start + 1: end]

    