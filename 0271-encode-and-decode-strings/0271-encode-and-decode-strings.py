class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = []
        for s in strs:
            ans.append(f"{len(s)}#{s}")
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        n = len(s)
        ans = []
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            ans.append(s[start:end])
            i = end
        return ans


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))