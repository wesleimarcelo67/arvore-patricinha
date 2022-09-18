from copyreg import constructor


class Node:
    def __init__(self, value):
        self.value = str(value)
        self.left = None
        self.right = None
        self.anchestor = None

    def isRadical(self, word):
        return self.value[0] == word[0]

    def getRadical(self, word):
        radical = ''
        index = 0
        while index < len(word):
            if self.value[index] == word[index]:
                radical += word[index] 
            else :
                break
            index += 1
        return radical

    def getSuffix(self, word):
        prefix = self.getRadical(word)
        return self.value.removeprefix(prefix)
    
    def hasChildren(self):
        return self.hasLeftChild() or self.hasRightChild()
    
    def hasLeftChild(self):
        return self.left is not None

    def hasRightChild(self):
        return self.right is not None