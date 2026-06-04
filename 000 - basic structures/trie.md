- 是否是某个词的前缀？
- 前缀长度？
- 是否是某个完整单词？

```python
# python语法不熟悉，此模板用于熟悉如何用python构建前缀树
root = {}
def insert(word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    
def search(word):
    node = root
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return True
```


