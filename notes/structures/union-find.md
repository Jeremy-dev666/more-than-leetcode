# 并查集 / Union-Find (Disjoint Set)

> **一句话 / TL;DR**:用「父指针数组」维护不相交集合,近 O(1) 完成合并(union)与查询是否同组(find),常用于求连通分量。

## 何时用 / When to use

- 求图的**连通分量个数**
- 判断两个节点是否连通 / 动态合并集合
- 「朋友圈」「岛屿合并」「冗余连接」一类问题

## 核心思想 / Core idea

每个集合用一棵树表示,树根作为集合代表。`find` 顺着父指针找到根(配合**路径压缩**把沿途节点直接挂到根上);`union` 把一个根挂到另一个根下,合并时连通分量数减一。

## 模板代码 / Template

求连通分量个数:

```java
int[] parent;

public int numberOfComponents(int n, int[][] edges) {
    parent = new int[n];
    for (int i = 0; i < n; i++) parent[i] = i;
    int count = n;
    for (int[] edge : edges) {
        int a = find(edge[0]);
        int b = find(edge[1]);
        if (a != b) {       // 不同集合才合并
            parent[a] = b;
            count--;
        }
    }
    return count;
}

private int find(int x) {
    if (parent[x] != x) {
        parent[x] = find(parent[x]);   // 路径压缩
    }
    return parent[x];
}
```

## 变体 / Variants

| 变体 | 关键区别 | 典型题 |
|---|---|---|
| BFS/DFS 数连通分量 | 不用并查集,遍历邻接表 | — |
| 按秩合并 | union 时挂矮树到高树,进一步优化 | — |

## 易错点 / Pitfalls

- `find` 的参数与函数体变量名要一致(原笔记此处有 `i`/`x` 不一致的 bug,已修正)
- 别忘了初始化 `parent[i] = i`
- 合并前必须先 `find` 到根,不能直接改 `parent[edge[0]]`

## 案例 / Problems

| # | 题目 | 难度 | 一句话考点 | 我的解法 |
|---|---|---|---|---|
| 200 | Number of Islands | Med | 网格连通分量 | [code](../../0200-number-of-islands/) |
| 323 | Number of Connected Components | Med | 模板裸题 | — |

## 关联 / Related

- 同问题的另一解法:BFS/DFS 遍历(见下方代码)

```java
// BFS 数连通分量(对照用)
private void bfs(List<List<Integer>> graph, int start, boolean[] visited) {
    Deque<Integer> queue = new ArrayDeque<>();
    queue.add(start);
    while (!queue.isEmpty()) {
        int node = queue.poll();
        for (int neighbor : graph.get(node)) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                queue.add(neighbor);
            }
        }
    }
}
```

<!-- 标签便于检索: #structure #union-find #graph -->
