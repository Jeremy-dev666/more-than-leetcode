# 前缀树 / Trie

> **一句话 / TL;DR**:用树形结构按字符逐层存储字符串集合,在 O(L) 内完成前缀查询、单词查询。

## 何时用 / When to use

- 是否是某个词的**前缀**?
- 前缀**长度**?
- 是否是某个**完整单词**?
- 大量字符串的公共前缀检索、自动补全、单词搜索

## 模板代码 / Template

```python
# 用嵌套 dict 构建前缀树(Python 简洁写法)
root = {}

def insert(word):
    node = root
    for char in word:
        if char not in node:
            node[char] = {}
        node = node[char]
    node["#"] = True        # 用哨兵键标记一个完整单词的结尾

def search(word):
    node = root
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return "#" in node      # 区分「是前缀」与「是完整单词」

def starts_with(prefix):
    node = root
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True
```

## 易错点 / Pitfalls

- 必须用**结尾标记**(如 `"#"`)区分「abc 是前缀」和「abc 是完整单词」,否则 search 与 starts_with 行为相同
- 原始模板缺失结尾标记,这里已补上

## 案例 / Problems

| # | 题目 | 难度 | 一句话考点 | 我的解法 |
|---|---|---|---|---|
| 208 | Implement Trie | Med | 模板裸题 | — |

<!-- 标签便于检索: #structure #trie #string -->
