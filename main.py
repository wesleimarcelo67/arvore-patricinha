from modules.node import Node
from modules.tree import PatriciaTree

str1= ''
str2 = 'bcaa'

node1 = Node(str1)

pt = PatriciaTree()

pt.addWord('banana')
pt.addWord('bandana')
pt.addWord('banda')
pt.addWord('bandada')



pt.print()


print(pt.nodes)




