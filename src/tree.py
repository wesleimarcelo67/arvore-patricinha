if __name__ == '__main__':
    from node import Node
else:
    from src.node import *


class PatriciaTree:

    def __init__(self):
        self.nodes = 0
        self.root = Node('---')

    def addWord(self, word):
        return self._addWord(self.root, word)

    def _addWord(self, node, word):
        if node is None:
            node.value = word
            self.nodes += 1
            return True
        else:
            if node == word:
                return False
            elif node.isRadical(word):
                radical = node.getRadical(word)
                nodeSuffix = node.getSuffix(word)
                wordSuffix = word.removeprefix(radical)

                if not node.hasChildren():
                    node.value = radical
                    if nodeSuffix < wordSuffix:
                        node.left = Node(nodeSuffix)
                        node.right = Node(wordSuffix)
                    else:
                        node.left = Node(wordSuffix)
                        node.right = Node(nodeSuffix)
                    self.nodes += 2
                    return True
                else :
                    if node.value < wordSuffix:
                        self._addWord(node.right, wordSuffix)
                    elif node.value > wordSuffix:
                        self._addWord(node.left, wordSuffix)

    def print(self):
        self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            print(node.value)
            if node.hasLeftChild():
                self._printTree(node.left)
            if node.hasRightChild():
                self._printTree(node.right)