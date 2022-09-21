if __name__ == '__main__':
    from nodes.internNode import Node
else:
    from modules.nodes.internNode import *
    from modules import helper


class PatriciaTree:

    def __init__(self):
        self.nodes: int = 0
        self.root: Node = None

    
    def _printTree(self, node: Node):
        if node is not None:

            if node.hasLeftChild():
                print(
                    f'node -> {node.left.value} | Index to go -> {node.left.indexToGo} | SubTree: Left')
                self._printTree(node.left)

            if node.hasRightChild():
                print(
                    f'node -> {node.right.value} | Index to go -> {node.right.indexToGo} | SubTree: Right')
                self._printTree(node.right)
