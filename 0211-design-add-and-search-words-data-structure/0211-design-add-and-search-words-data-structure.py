class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(index: int, node: Node) -> bool:
            if index == len(word):
                return node.end

            c = word[index]
            if c != '.':
                if c not in node.son:
                    return False
                return dfs(index+1, node.son[c])
            else:
                for child in node.son.values():
                    if dfs(index+1, child):
                        return True
                return False

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)