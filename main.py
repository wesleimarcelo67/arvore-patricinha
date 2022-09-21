from modules.tree import PatriciaTree


str1 = {'value' : 'a'}
str2 = str1

str1 = 'b'
str2 = str1

pt = PatriciaTree()


print(pt.insert('casamento'))
print(pt.insert('casa'))
print(pt.insert('casaea'))
print(pt.insert('casay'))


pt.print()





