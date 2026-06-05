class MaxStack {
    class Node {
        int val;
        Node prev;
        Node next;
        Node (int val) {
            this.val = val;
        }
    }

    Node dummy = new Node(-1);
    TreeMap<Integer, Deque<Node>> map;

    public MaxStack() {
        dummy.prev = dummy;
        dummy.next = dummy;
        map = new TreeMap<>();
    }
    
    public void push(int x) {
        Node node = new Node(x);
        node.prev = dummy.prev;
        node.next = dummy;
        node.prev.next = node;
        node.next.prev = node;
        map.computeIfAbsent(x, k -> new ArrayDeque<>()).push(node);
    }
    
    public int pop() {
        Node lastNode = dummy.prev;
        removeNode(lastNode);
        Deque<Node> dq = map.get(lastNode.val);
        // 删的是栈里最后加进来的
        dq.pop();

        if (dq.isEmpty()) map.remove(lastNode.val);
        return lastNode.val;
    }
    
    public int top() {
        return dummy.prev.val;
    }
    
    public int peekMax() {
        return map.lastKey();
    }
    
    public int popMax() {
        int maxVal = map.lastKey();
        Deque<Node> dq = map.get(maxVal);
        Node delNode = dq.pop();
        // 记得查一下这个栈pop完是否为空，空要在map中删掉
        if (dq.isEmpty()) map.remove(maxVal);
        removeNode(delNode);
        return maxVal;
    }

    private void removeNode(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */