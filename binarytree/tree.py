class BinaryTreeNode:
    def __init__(self,data):
		self.root=data
		self.leftchild=None
		self.rightchild=None
    def insertLeft(self,data):
        if self.leftchild==None:
            self.leftchild = BinaryTreeNode(data)
        else:
            t=BinaryTreeNode(data)
            t.leftchild = self.leftchild
            self.leftchild=t
    def insertRight(self,data):
        if self.rightchild==None:
            self.rightchild = BinaryTreeNode(data)
        else:
            t=BinaryTreeNode(data)
            t.rightchild = self.rightchild
            self.rightchild=t
    def setRoot(self,data):
		self.root=data
    def getRoot(self):
		return self.root
    def getLeft(self):
		return self.leftchild
    def getRight(self):
		return self.rightchild

def postorder(node,result):
    if not node:
        return
    postorder(node.leftchild,result)
    postorder(node.rightchild,result)
    result.append(node.root)
    
