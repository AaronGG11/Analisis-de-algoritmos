from queue import PriorityQueue
from binaryTree import *

mypq = PriorityQueue()


mypq.put((18.3,"_"))
mypq.put((10.2,"e"))
mypq.put((7.7,"t"))
mypq.put((6.8,"a"))
mypq.put((5.9,"o"))
mypq.put((5.8,"i"))
mypq.put((5.5,"n"))
mypq.put((5.1,"s"))
mypq.put((4.9,"h"))
mypq.put((4.8,"r"))
mypq.put((3.5,"d"))
mypq.put((3.4,"l"))
mypq.put((2.6,"c"))
mypq.put((2.4,"u"))
mypq.put((2.1,"m"))
mypq.put((1.9,"w"))
mypq.put((1.8,"f"))
mypq.put((1.7,"g"))
mypq.put((1.6,"y"))
mypq.put((1.6,"p"))
mypq.put((1.3,"b"))
mypq.put((0.9,"v"))
mypq.put((0.6,"k"))
mypq.put((0.2,"j"))
mypq.put((0.2,"x"))
mypq.put((0.1,"q"))
mypq.put((0.1,"z"))


#mya = searchtree()
contador = mypq.get()[0] + mypq.get()[0]
print(contador)


'''
tree = searchtree()     
arr = [8,3,1,6,4,7,10,14,13]
for i in arr:
    tree.create(i)
print('Breadth-First Traversal')
tree.bft()
print('Inorder Traversal')
tree.inorder(tree.root) 
print('Preorder Traversal')
tree.preorder(tree.root) 
print('Postorder Traversal')
tree.postorder(tree.root)
print('BFS')
tree.bft()



print(mypq.counter)

'''