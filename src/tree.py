if __name__ == '__main__':
    from node import Node
else:
    from src.node import *


class PatriciaTree:

    def __init__(self):
        self.nodes = 0
        self.root = None

    def addWord(self, word):
        if self.root is None:
            self.root = Node(word)
            self.nodes += 1
            return True
        else:
            if self.root == word:
                return False
            elif self.root.isRadical(word):
                radical = self.root.getRadical(word)
                rootSuffix = self.root.getSuffix(word)
                wordSuffix = word.removeprefix(radical)

                if not self.root.hasChildren():
                    self.root.value = radical
                    if rootSuffix < wordSuffix:
                        self.root.left = Node(rootSuffix)
                        self.root.right = Node(wordSuffix)
                    else:
                        self.root.left = Node(wordSuffix)
                        self.root.right = Node(rootSuffix)
                    self.nodes += 2

    def print(self):
        self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            print(node.value)
            if node.hasLeftChild():
                self._printTree(node.left)
            if node.hasRightChild():
                self._printTree(node.right)