class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        n = len(s)
        MX = pow(2, 31) - 1
        MN = -pow(2, 31)

        idx = 0
        while idx < n and s[idx] == " ":
            idx += 1
        
        sign = 1
        if idx < n and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < n and s[idx] == "-":
            sign = -1
            idx += 1
        
        while idx < n and s[idx].isdigit():
            digit = int(s[idx])
            if (ans == MX // 10 and digit > MX % 10) or (ans > MX // 10):
                return MX if sign == 1 else MN
            ans = 10 * ans + digit
            idx += 1

        return ans * sign