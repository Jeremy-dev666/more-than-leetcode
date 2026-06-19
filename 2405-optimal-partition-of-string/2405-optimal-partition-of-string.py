class Solution:
    def partitionString(self, s: str) -> int:
        lastIdx = [-1]*26
        cnt = 1
        start = 0

        for i in range(len(s)):
            # 验证当前字母是否在窗口内
            if lastIdx[ord(s[i]) - ord('a')] >= start:
                cnt += 1
                start = i
            lastIdx[ord(s[i]) - ord('a')] = i

        return cnt