from src.node import Node
from src.tree import PatriciaTree

str1= 'baa'
str2 = 'bcaa'

node1 = Node(str1)

pt = PatriciaTree()

pt.addWord('waldeco')
pt.addWord('waldeci')

pt.print()


print(pt.nodes)




