class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        # Your Code Here
        def isIdentical(root1, root2):
            if root1 is None and root2 is None:
                return 1
        
            if root1 is not None and root2 is not None:
                
                if(root1.data!=root2.data):
                    return 0
                    
            if(root1==None or root2==None):
                return 0
                
            return isIdentical(root1.left,root2.right) and isIdentical(root1.right,root2.left)
            
        if(root==None):
            return True
        # if there is just 1 node in the tree, then obvisously it is symmetric
        if(not root.right and not root.left):
            return True
            
        return isIdentical(root.left,root.right)
        