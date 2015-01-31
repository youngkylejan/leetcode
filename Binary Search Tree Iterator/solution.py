# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    def __init__(self, root):
    	self.root = root
    	self.array = []       
    	self.nextIndex = 0
    	self.inorderTraversal(self.root)
    
    def inorderTraversal(self, root):
    	if root is not None:
    		self.inorderTraversal(root.left)
    		self.array.append(root.val)
    		self.inorderTraversal(root.right)
    
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
    	if self.nextIndex < len(self.array):
    		return True
    
    # @return an integer, the next smallest number
    def next(self):
    	self.nextIndex = self.nextIndex + 1
    	return self.array[self.nextIndex - 1]


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())