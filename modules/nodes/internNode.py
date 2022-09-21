if __name__ == '__main__':
    from node import Node
else:
    from modules.nodes.node import Node


class InternNode(Node):
    def __init__(self, value: str = None, indexToGo: int = -1):
        self.value: str = value
        self.indexToGo: int = indexToGo
        self.left = None
        self.right = None

    def getRadical(self, word) -> str:
        radical = ''
        index = 0

        while index < len(word) and index < self.getLength():
            if self.value[index] == word[index]:
                radical += word[index]
            else:
                break
            index += 1

        return radical

    def getSuffix(self, word):
        prefix = self.getRadical(word)
        return self.value.removeprefix(prefix)

    def hasChildren(self) -> bool: return self.hasLeftChild() or self.hasRightChild()

    def hasLeftChild(self) -> bool: return self.left is not None

    def hasRightChild(self) -> bool: return self.right is not None

    def getLength(self) -> int: return len(self.value)
