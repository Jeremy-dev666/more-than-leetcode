ALPHA = 'abcdefghijklmnopqrstuvwxyz'

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 这一步很重要，查询单词是否存在，用集合比列表快
        wordList = set(wordList)
        
        if endWord not in wordList:
            return 0

        # hashset
        begin_side, end_side = {beginWord}, {endWord}
        visited = {beginWord, endWord}
        step = 1

        while begin_side and end_side:
            if begin_side > end_side:
                begin_side, end_side = end_side, begin_side

            layer_set = set()
            step += 1
            for word in begin_side:
                for i in range(len(word)):
                    # 尝试替换26个字母
                    for c in ALPHA:
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in end_side:
                            return step

                        if new_word in wordList and new_word not in visited:
                            layer_set.add(new_word)
                            visited.add(new_word)
            
            begin_side = layer_set

        return 0