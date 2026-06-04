class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # positive integer in arr
        # 123 is prefix of 12345
        # 5655 is a common prefix of 5655359 and 56554
        # return longest length of common prefix of all pairs

        # build trie
        root = {}
        for num in arr2:
            node = root
            for c in str(num):
                if c not in node:
                    node[c] = {}
                node = node[c]
        
        ans = 0
        for num in arr1:
            node = root
            length = 0
            for c in str(num):
                if c not in node:
                    break
                node = node[c]
                length += 1
            ans = max(ans, length)

        return ans