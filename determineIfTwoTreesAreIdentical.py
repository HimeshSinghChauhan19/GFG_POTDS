'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        
        if root1 is None and root2 is None:
            return 1
        
        if root1 is not None and root2 is not None:
            
            if(root1.data!=root2.data):
                return 0
        if(root1==None or root2==None):
            return 0
            
        return self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
        
        
