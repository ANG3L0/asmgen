from mynode import *

if __name__ == '__main__':
	root = Node()
	tmpNode = Node()
	#tmpNode.setData('test1')
	tmpNode.data = 'test1'
	tmpNode.setParent(root)
	root.setChildren([tmpNode, tmpNode])
	a = root.getChildren()
	print a[0].getParent().getChildren()

