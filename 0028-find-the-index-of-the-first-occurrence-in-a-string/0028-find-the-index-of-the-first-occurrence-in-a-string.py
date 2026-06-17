class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr = 0
        n, m = len(haystack), len(needle)
        while ptr < n:
            if haystack[ptr] == needle[0]:
                if haystack[ptr:ptr+m] == needle:
                    return ptr
            ptr += 1
        return -1
