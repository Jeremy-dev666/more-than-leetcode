/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return node;

        // value = index and start with 1
        Queue<Node> q = new LinkedList<>();
        q.add(node);
        Map<Node, Node> visited = new HashMap<>();
        visited.put(node, new Node(node.val, new ArrayList()));

        while (!q.isEmpty()) {
            Node cur = q.remove();
            for (Node nb : cur.neighbors) {
                if (!visited.containsKey(nb)) {
                    visited.put(nb, new Node(nb.val, new ArrayList()));
                    q.add(nb);
                }
                visited.get(cur).neighbors.add(visited.get(nb));
            }
        }
        return visited.get(node);
    }
}