import abc 
from abc import ABC, abstractmethod 

import operator
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        # suppose to evaluate the tree's value
        pass

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': lambda a, b: int(a / b)
}

class NumberNode(Node):
    def __init__(self, val: int):
        self.val = val

    def evaluate(self) -> int:
        return self.val

class OperatorNode(Node):
    def __init__(self, op: str, left: Node, right: Node):
        self.func = OPS[op]
        self.left = left
        self.right = right
    
    def evaluate(self) -> int:
        return self.func(self.left.evaluate(), self.right.evaluate())


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree representing it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        st = []
        for token in postfix:
            if token in OPS:
                right = st.pop()
                left = st.pop()
                st.append(OperatorNode(token, left, right))
            else:
                st.append(NumberNode(int(token)))

        return st.pop()

		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
        