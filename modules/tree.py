if __name__ == '__main__':
    from nodes.internNode import *
    from nodes.leaf import *
else:
    from modules.nodes.internNode import *
    from modules.nodes.leaf import *
    from modules import helper


class PatriciaTree:

    def __init__(self):
        self.nodes: int = 0
        self.root: Node = None

    def insert(self, word):

        if self.root == None:
            self.root = Leaf(word)
            return True
        else:
            node = self.root
            while True:
                IS_LEAF = isinstance(node, Leaf)

                if IS_LEAF:
                    if node.value == word:
                        return False
                    else:           

                        nodeValue = node.value
                        index = helper.getMismatchIndex(nodeValue, word)
                        nodeChar = helper.getCharAtIndex(nodeValue, index)
                        wordChar = helper.getCharAtIndex(word, index) 

                        IS_ROOT = node.ancestor == None

                        if IS_ROOT:
                            char = helper.getSmaller(nodeChar, wordChar)
                            self.root = InternNode(index, char)
                            node = self.root
                        else:
                            print('it is not root')
                        if nodeChar > wordChar:
                            node.leftChild = Leaf(word)
                            node.rightChild = Leaf(nodeValue)
       
                        
                        if nodeChar < wordChar:
                            node.leftChild = Leaf(nodeValue)    
                            node.rightChild = Leaf(word)
                        
                        node.rightChild.ancestor = node
                        node.leftChild.ancestor = node
                        
                        return True                            
                else:
                    nodeChar = node.dismatchedChar

                    index = node.indexToGo
                    wordChar = helper.getCharAtIndex(word, index)

                    if wordChar > nodeChar:
                        node = node.rightChild
                    else:
                        node = node.leftChild


    def search(self, word):
        pass

    def remove(self, word):
        pass

    
    def print(self):
        if self.root == None:
            print('Arvore Vazia')
        else:
            self._printTree(self.root, 'Root' )


    def _printTree(self, node: Node, subtree):
        if Node is not None:
            if isinstance(node, Leaf):
                print(f'node -> {node.value} | subtree: {subtree} | Ancestor: {node.ancestor.dismatchedChar}')
            
            elif isinstance(node, InternNode):
                self._printTree(node.leftChild, 'left')
                self._printTree(node.rightChild, 'right')

