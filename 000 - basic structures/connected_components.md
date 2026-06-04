## BFS
```java
public class Solution { 
    public static int numberOfComponents(int n, int[][] edges) { 
        // 建立邻接表
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
        // 记录访问状态
        boolean[] visited = new boolean[n];
        int count = 0;
        // 节点入口
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(graph, i, visited);
                count++;
            }
        }
        return count;
    }

    private static void bfs(List<List<Integer>> graph, int start, boolean[] visited) { 
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
}
```

## Union Find
```java
public class Solution { 
    public static int numberOfComponents(int n, int[][] edges) { 
        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        int count = n;
        for (int[] edge : edges) {
            // 找爸爸
            int a = find(parent, edge[0]);
            int b = find(parent, edge[1]);
            // 建立连通关系
            if (a != b) {
                parent[a] = b;
                count--;
            }
        }
        return count;
    }

    private static int find(int[] parent, int i) { 
        // 自己不是爸爸，找爸爸
        if (parent[x] != x) {
            parent[x] = find(parent, parent[x]);
        }
        // 返回爸爸是谁
        return parent[x];
    }
}
```