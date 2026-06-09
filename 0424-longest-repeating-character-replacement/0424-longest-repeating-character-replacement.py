from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        max_freq = 0
        left = right = 0
        while right < len(s):
            c = s[right]
            freq[c] += 1
            max_freq = max(max_freq, freq[c])

            if right - left + 1 - max_freq > k:
                del_c = s[left]
                freq[del_c] -= 1
                left += 1

            ans = right - left + 1
            right += 1

        return ans