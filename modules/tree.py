if __name__ == '__main__':
    from node import Node
else:
    from modules.node import *
    from modules import helper 


class PatriciaTree:

    def __init__(self):
        self.nodes: int = 0
        self.root: Node = Node()
       

    def insert(self, word: str):
        isTreeEmpty = self.root.hasChildren() is False
        if isTreeEmpty:
            self.root.value = word[0]
            self.root.indexToGo = 0
            self.root.left = Node(word)
        else:
           print('tem filhos') 
    
    def search(self,word):
        node = self.root

        if node.indexToGo == -1:
            print('arvore vazia')
        else:
            index = node.indexToGo
            while node is not None:
                if node.value == word:
                    print('Palavra encontrada!')
                    print(f'Valor: {node.value}')
                    return
                else:
                    if word[index] > node.value:
                        node = node.right
                    elif word[index] <= node.value:
                        node = node.left
        print('Palavra nao encontrada')

    def print(self):
        print(f'Root -> {self.root.value} | Index to go -> {self.root.indexToGo}')
        self._printTree(self.root)

    def _printTree(self, node: Node):
        if node is not None:

            if node.hasLeftChild():
                print(f'node -> {node.left.value} | Index to go -> {node.left.indexToGo} | SubTree: Left')
                self._printTree(node.left)
            
            if node.hasRightChild():
                print(f'node -> {node.right.value} | Index to go -> {node.right.indexToGo} | SubTree: Right')
                self._printTree(node.right)
