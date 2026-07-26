ROMAN = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for a, b in pairwise(s):
            a, b = ROMAN[a], ROMAN[b]
            ans += a if a >= b else -a

        return ans + ROMAN[s[-1]]