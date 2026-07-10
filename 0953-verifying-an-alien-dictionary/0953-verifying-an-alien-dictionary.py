class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # 字母映射索引
        mp = {c: idx for idx, c in enumerate(order)}

        # 将单词转化为数字
        word_to_num = []
        for w in words:
            path = []
            for c in w:
                path.append(mp[c])
            word_to_num.append(path)

        # 比较
        for i in range(len(word_to_num) - 1):
            cur = word_to_num[i]
            nxt = word_to_num[i + 1]
            if cur > nxt:
                return False

        return True



        