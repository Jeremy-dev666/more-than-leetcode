# 并查集 / Union-Find (Disjoint Set Union)

> 起因:LeetCode 684 (Redundant Connection)。之前一直以为并查集只是"数连通分量"的工具,684 让我意识到:**`union` 的返回值本身就是信息**——合并失败(两点已同根)意味着这条边是多余的,加上它必然成环。数连通分量只是它最浅的一层用法。

## 一句话结论

**并查集维护的是一个动态的等价关系:支持"合并两个集合"和"查询两元素是否同组",两个操作均摊近 O(1)。凡是问题能翻译成"元素分组 + 组会不断合并",它就适用——连通只是"等价"最常见的具体化。**

它的能力边界也由此决定:**只能合并,不能分裂**;只回答"是否同组",不回答"怎么走过去"(路径)。这两条决定了它什么时候碾压 BFS/DFS、什么时候完全无能为力(见选型速查)。

## 核心思想 / Core idea

每个集合是一棵树,根节点作为集合的代表元。`find(x)` 沿父指针爬到根;`union(a, b)` 把一棵树的根挂到另一棵的根下。判断同组 = 判断同根。

朴素实现的树可能退化成链,`find` 变成 O(n)。两个优化各砍一刀:

- **路径压缩**:`find` 返回途中把沿路节点直接挂到根上,树越查越扁;
- **按秩合并**:`union` 时让矮树挂到高树下,树高只在两树同高时 +1,增长是对数级的。

两者叠加后单次操作均摊 O(α(n)),α 是反阿克曼函数,宇宙尺度的 n 也不超过 5——工程上当常数看。只用其中一个优化也能到 O(log n),刷题够用,但模板反正就几行,建议两个都带上。

## 模板代码 / Template

以 684/323 的实现为骨架,三个关键设计:`union` 返回 bool(是否真的发生了合并)、维护 `cnt`(当前集合数)、路径压缩 + 按秩合并齐全。这一个模板同时服务下面所有用法:

```python
class UF:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.cnt = n                  # 当前集合数,union 成功一次减一

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # 路径压缩
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False              # 已同组:这条边是"多余的"(见用法 3)
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra           # 保证 ra 是高树
        self.parent[rb] = ra          # 矮树挂高树
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.cnt -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)
```

> 递归版 `find` 在链很长时可能爆栈(Python 默认递归深度 1000),数据规模大时换迭代写法:先爬到根,再第二遍沿路把 parent 全部指向根。

## 它都能干什么 / Applications

按"离连通分量有多远"排序,越往后越体现并查集独有的价值。

### 1. 数连通分量(最基础)

初始 n 个集合,每条边 `union` 一次,最后 `cnt` 就是答案(323)。网格题(200)把 `(r, c)` 编码成 `r * cols + c` 后同理——但注意这类**静态图**上 BFS/DFS 同样 O(V+E),并查集只是写起来短,并无本质优势。

### 2. 连通性查询

建好之后 `connected(a, b)` 近 O(1) 回答"a 和 b 是否连通",且**边可以随时继续加**。查询和加边交错出现时,BFS 每次查询都要重新遍历,并查集每次只动几个指针——这是分水岭的开始。

### 3. 环检测 / 冗余边(684 的洞察)

无向图加边过程中,`union(a, b)` 返回 `False` ⟺ a、b 早已连通 ⟺ 边 `(a, b)` 与已有路径构成环。**不需要任何额外逻辑,环检测是 union 语义的免费副产品**:

```python
for a, b in edges:
    if not uf.union(a, b):
        return [a, b]        # 684:第一条使图成环的边
```

684 要求"多条冗余边时返回最后一条",按输入顺序逐条 union、返回第一次失败的那条,恰好满足——因为前面的边都成功合并了,失败的这条一定是"最后出现的冗余边"。

### 4. 判树(环检测的直接推论)

n 个点的无向图是树 ⟺ 恰好 n-1 条边 且 无环(或:n-1 条边 且 连通,二者在边数固定时等价)。261 (Graph Valid Tree) 用并查集就是:先查 `len(edges) == n - 1`,再逐条 union,任何一次失败即有环、返回 False。我当时用的是 BFS 数可达点([code](../../0261-graph-valid-tree/)),并查集解法更短,且不用建邻接表。

### 5. Kruskal 最小生成树

Kruskal = 边按权重排序 + 逐条尝试 union:成功就选入 MST,失败(成环)就丢弃,选满 n-1 条为止。并查集在这里扮演的角色和 684 一模一样——**高效判断"这条边加进来会不会成环"**。684 本质上就是 Kruskal 的内循环单独拿出来考。典型题:1584 (Min Cost to Connect All Points)。

### 6. 等价类合并(跳出"图"的字面意义)

并查集维护的是抽象的**等价关系**(自反、对称、传递),不一定要有真的图:

- **990 (Satisfiability of Equality Equations)**:`a==b` 就 union,处理完再检查每个 `a!=b` 是否被迫同组——同组即矛盾;
- **721 (Accounts Merge)**:email 出现在同一账户 → union,等价类就是同一个人。实现技巧([code](../../0721-accounts-merge/)):**union 的元素是账户下标而不是邮箱**,邮箱只做 `email → 首次所属账户` 的映射,再次见到同一邮箱就 union 两个账户——省掉给邮箱离散化的一层;
- **547 (Number of Provinces)**:朋友关系的传递闭包分组。

识别信号:题面出现"传递性"——a 和 b 一伙、b 和 c 一伙 ⟹ a 和 c 一伙。看到这个结构,把"一伙"翻译成 union 即可,元素是什么(变量、邮箱、人)无所谓。字符串/对象做元素时用 `dict` 版 parent 或先离散化成下标。

### 7. 动态加边 / 在线问题(并查集不可替代的主场)

**305 (Number of Islands II)**:每放一块陆地,报告当前岛屿数。BFS/DFS 每次操作后都得全图重扫,O(k·mn);并查集只需新增一个点、和四邻居 union,`cnt` 实时就是答案,O(k·α)。**"过程中每一步都要答案"的增量连通问题,是并查集与遍历法真正拉开数量级差距的地方**——前面的静态题它只是"更顺手",这里它是唯一解。

### 8. 离线倒序:用"合并"模拟"删除"

并查集不能分裂,但**删边问题若允许离线(所有操作预先已知),把时间倒放,删边就变成加边**:先构建删完所有边后的终态,再逆序把边一条条 union 回去,倒序回答查询。典型:"依次断开这些边,每次断开后还连通吗"。这是把工具的短板绕过去的经典手法,识别关键词:**离线 + 删除/摧毁 + 连通性**。

### 9. 带权并查集(进阶)

父指针上附加一个"相对权值",`find` 压缩路径时同步累积。能回答的不再是"是否同组",而是"同组的话,a 相对 b 的比值/差值是多少"。典型:399 (Evaluate Division),`a/b=2, b/c=3` ⟹ 回答 `a/c=6`。信号:等价关系之上还叠了一层**可传递的量化关系**。

实现要点([code](../../0399-evaluate-division/)),约定 `weight[x] = x / parent(x)`,三处都围绕这个不变量:

- **find 压缩路径时权值同步相乘**:`(儿子/爸爸) × (爸爸/爷爷) = 儿子/爷爷`,压缩后 `weight[x]` 直接表示 `x / root`;
- **union 挂接时解方程定权值**:把 `rb` 挂到 `ra` 下,由 `a/b = val` 推出 `weight[rb] = weight[a] / (val × weight[b])`;
- **query 同根才可答**:`a/b = weight[a] / weight[b]`(两者都已压缩到同一根),不同根返回 -1。

字符串变量先用 dict 离散化成下标,正是用法 6 说的那套。

## 什么时候不用 / When NOT to use

- **有向图**:连通(等价关系)是对称的,而有向可达不对称——`a→b` 不代表 `b→a`,union 一做就把方向信息抹掉了。207/210 (Course Schedule) 问的是有向图有没有环,必须拓扑排序/DFS 染色;1462 问有向可达性,用 Floyd 传递闭包或 BFS([code](../../1462-course-schedule-iv/))。**"课程表系列不能用并查集"是最常见的误用点。**
- **需要路径本身**:并查集只知道"通",不知道"怎么通"。要最短路/具体路径,BFS(见 [BFS vs DFS 最短路](../patterns/bfs-vs-dfs-shortest-path.md))或 Dijkstra。
- **在线删边**:必须实时支持"断开再查询"且不能离线倒序时,并查集无能为力(那是 Link-Cut Tree 的领域,竞赛级,刷题不涉及)。

## 易错点 / Pitfalls

- **合并根,不是合并元素**:`union` 里必须先 `find` 到两个根再挂接;直接 `parent[a] = b` 只改了 a 自己,a 原来的子树没跟过来。
- **忘了初始化 `parent[i] = i`**:每个元素初始必须自成一组。
- **节点编号从 1 开始的题**(684 就是):数组要开 `n + 1`,或统一减一。开小了越界,开大了浪费但不错——684 我的实现开的 `n + 1` 就是为此。
- **按秩合并时 rank 的更新条件**:只有两树 rank 相等、其中一棵被迫长高时才 `+= 1`;无脑加会让 rank 失真,退化成随机挂接(不算错,但优化就没了)。
- **递归 find 爆栈**:Python 链长超过 1000 就 RecursionError,大数据换迭代版。
- **用 `parent[x] == x` 判根之前必须先压缩**:想统计"有多少个不同的组"时,要么用 `cnt` 计数器,要么对每个元素调一次 `find` 再数不同的根——直接数 `parent[i] == i` 在没有全部 find 过时是对的(根的 parent 永远是自己),但数 `len(set(parent))` 是错的,未压缩的中间节点会虚增组数。

## 选型速查 / Union-Find vs BFS/DFS

| 问题特征 | 工具 | 原因 |
|---|---|---|
| 静态无向图,一次性数连通分量 | 都行 | 复杂度同级,UF 代码短,BFS/DFS 不用额外结构 |
| 边动态增加 + 过程中反复查询/报数 | **并查集** | 增量 O(α) vs 每次全图重扫 |
| 加边过程中判环 / 找冗余边 / Kruskal | **并查集** | 环检测是 union 的免费副产品 |
| "传递性分组"(等价类),未必有显式图 | **并查集** | 等价关系是它的本命抽象 |
| 离线删边 + 连通性 | **并查集(时间倒流)** | 删除倒放成合并 |
| 要最短路 / 路径本身 / 层数 | BFS | UF 不保存路径信息 |
| 有向图(拓扑序、有向环、可达性) | 拓扑排序 / DFS / Floyd | 连通对称,有向不对称,UF 直接不适用 |

触发信号一句话:**"不断合并、只增不减、反复问是否同组/共几组"** → 并查集。

## 案例 / Problems

| # | 题目 | 难度 | 一句话考点 | 我的解法 |
|---|---|---|---|---|
| 323 | Number of Connected Components | Medium | 数连通分量模板裸题 | [code](../../0323-number-of-connected-components-in-an-undirected-graph/) |
| 200 | Number of Islands | Medium | 网格连通分量,坐标编码成一维 | [code](../../0200-number-of-islands/) |
| 261 | Graph Valid Tree | Medium | 判树 = n-1 条边 + 无环;我用的 BFS,UF 更短 | [code](../../0261-graph-valid-tree/) |
| 684 | Redundant Connection | Medium | union 失败 ⟺ 成环,环检测零额外代码 | [code](../../0684-redundant-connection/) |
| 547 | Number of Provinces | Medium | 等价类分组 | 待刷 |
| 990 | Satisfiability of Equality Equations | Medium | 先 union 所有等式,再用不等式找矛盾 | 待刷 |
| 721 | Accounts Merge | Medium | 账户下标做元素、邮箱做"胶水"的等价类合并 | [code](../../0721-accounts-merge/) |
| 305 | Number of Islands II | Hard | 在线加点报岛数,UF 不可替代的场景 | 待刷 |
| 1584 | Min Cost to Connect All Points | Medium | Kruskal,684 的完整版 | 待刷 |
| 399 | Evaluate Division | Medium | 带权并查集,权值 = 到父节点的比值 | [code](../../0399-evaluate-division/) |

## 关联 / Related

- 对比:[BFS vs DFS 最短路](../patterns/bfs-vs-dfs-shortest-path.md)——静态图上互为替代,动态/增量场景 UF 胜,要路径 BFS 胜
- 反例:课程表系列(207/210/1462)是有向图,UF 不适用,归拓扑排序
- 进阶思想:离线倒序(时间倒流)不止用于并查集,是一类通用技巧

<!-- 标签便于检索: #structure #union-find #dsu #graph #connectivity #kruskal -->
