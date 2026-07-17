class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        ans = 0

        def countP(start, end):
            cnt = 0
            while start >= 0 and end < n and s[start] == s[end]:
                cnt += 1
                start -= 1
                end += 1
            return cnt


        # 奇偶回文
        for i in range(n):
            ans += countP(i, i)
            ans += countP(i, i+1)

        return ans