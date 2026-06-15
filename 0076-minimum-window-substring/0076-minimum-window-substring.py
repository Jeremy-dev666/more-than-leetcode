
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        freq = [0] * 128
        types = 0

        for i in range(n):
            idx = ord(t[i])
            if freq[idx] == 0:
                types += 1
            freq[idx] += 1

        
        start = left = right = 0
        min_len = float('inf')
        w = [0] * 128
        valid = 0
        while right < m:
            idx = ord(s[right])
            w[idx] += 1
            if freq[idx] != 0 and w[idx] == freq[idx]:
                valid += 1

            while valid == types:
                cur_len = right - left + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start = left

                l_idx = ord(s[left])
                w[l_idx] -= 1
                if freq[l_idx] != 0 and freq[l_idx] > w[l_idx]:
                    valid -= 1
                left += 1
            right += 1

        return s[start:(start + min_len)] if min_len != float('inf') else ""