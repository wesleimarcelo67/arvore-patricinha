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
        else:
            node = self.root

            while True:
                IS_EQUALS = node.value == word

                if IS_EQUALS:
                    break

                elif node.isRadical(word):
                    radical = node.getRadical(word)
                    nodeSuffix = node.getSuffix(word)
                    wordSuffix = word.removeprefix(radical)

                    if not node.hasChildren():
                        node.value = radical
                        if nodeSuffix < wordSuffix:
                            if nodeSuffix != '':
                                node.left = Node(nodeSuffix)
                            if wordSuffix != '':
                                node.right = Node(wordSuffix)
                        else:
                            if wordSuffix != '':
                                node.left = Node(wordSuffix)
                            if nodeSuffix != '':
                                node.right = Node(nodeSuffix)
                        self.nodes += 2
                        break
                    else:
                        if node.value < wordSuffix:
                           node = node.right
                        elif node.value > wordSuffix:
                           node = node.left
                        word = wordSuffix
                else: 
                    break        

    def print(self):
        self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            print(f'node -> {node.value}')
            if node.hasLeftChild():
                self._printTree(node.left)
            if node.hasRightChild():
                self._printTree(node.right)
