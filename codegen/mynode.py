class Node(object):
	def __init__(self):
		self.children = []
		self.data = ''
		self.parent = []
		self.lineNum = -1
	def getChildren(self):
		return self.children
	def getParent(self):
		return self.parent
	def setChildren(self, newChildren):
		self.children = newChildren
	def setParent(self, parent):
		self.parent = parent
	def setData(self,data):
		self.data = data
	def setLineNum(self,lineNum):
		self.lineNum = lineNum
	def getData(self):
		return self.data
	def isLeaf(self):
		return self.children==[]
	def isProgram(self):
		return self.data==''
	def isOrphan(self):
		return self.parent==[] #either parent is an empty list or one node.
