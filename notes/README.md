# 算法知识库 / Algorithm Knowledge Base

以**算法套路**为主体的刷题笔记库。每刷一题,回到对应套路笔记往「案例」表加一行,而非新建文件;只有真正值得长篇展开的硬题才进 `deep-dives/`。

## 怎么用 / Workflow

1. 刷完一题 → 判断它属于哪个套路 → 打开 `patterns/对应.md`,在「案例」表加一行
2. 该套路还没有笔记 → 复制 `_TEMPLATE-pattern.md` 新建一份
3. 题目曲折/多解法值得深挖 → 复制 `_TEMPLATE-deep-dive.md` 进 `deep-dives/`,并从套路笔记链接过去
4. 链接统一用**标准 Markdown 相对路径**(GitHub 可点),标签用 `#tag` 便于搜索

## 目录 / Structure

- `patterns/` — 套路纲领笔记(主体)
- `structures/` — 数据结构笔记
- `deep-dives/` — 少量硬题单题深挖
- `_TEMPLATE-*.md` — 模板

## 套路地图 / Pattern Map

掌握程度:🟢 熟练 / 🟡 会做但不熟 / 🔴 待补

| 套路 | 笔记 | 掌握 |
|---|---|---|
| 单调栈 Monotonic Stack | [link](./patterns/monotonic-stack.md) | 🟡 |
| 二分查找 Binary Search | [link](./patterns/binary-search.md) | 🟡 |
| 前缀和 & 差分 Prefix Sum | [link](./patterns/prefix-sum-2d.md) | 🟡 |
| 滑动窗口 Sliding Window | — | 🔴 |
| 双指针 Two Pointers | — | 🔴 |
| 回溯 Backtracking | — | 🔴 |
| 扫描线 Sweep Line | — | 🔴 |
| 动态规划 DP | — | 🔴 |
| BFS / DFS | [link](./patterns/bfs-vs-dfs-shortest-path.md) | 🟡 |
| 双向 BFS Bidirectional BFS | [link](./patterns/bidirectional-bfs.md) | 🟡 |

## 数据结构 / Structures

| 结构 | 笔记 |
|---|---|
| 前缀树 Trie | [link](./structures/trie.md) |
| 并查集 Union-Find | [link](./structures/union-find.md) |
| 基础排序 Elementary Sorts | [link](./structures/sorting-basics.md) |

## 深挖 / Deep Dives

| # | 题目 | 套路 |
|---|---|---|
| 42 | Trapping Rain Water | 单调栈 / 双指针 |
