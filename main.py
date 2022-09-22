from modules.tree import PatriciaTree


str1 = {'value' : 'a'}
str2 = str1

str1 = 'b'
str2 = str1

pt = PatriciaTree()


pt.insert('casa')
pt.insert('casamento')
pt.insert('casae')
pt.insert('casaei')
pt.insert('casati')



pt.print()


