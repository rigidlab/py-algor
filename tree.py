class BinaryTreeNode:
	def __init__(self,data):
		self.root=data
		self.left=None
		self.right=None
	
	def setRoot(self,data):
		self.root=data
	
	def getRoot(self):
		return self.root
	
	def getLeft(self):
		return self.left
	
	def getRight(self):
		return self.right
