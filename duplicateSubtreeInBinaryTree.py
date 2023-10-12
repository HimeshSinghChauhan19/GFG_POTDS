class Solution:
    
    dp={}    
    def dupRecur(self,root):
        if root==None:
            return ""
        left=self.dupRecur(root.left)
        mid=str(root.data)
        right=self.dupRecur(root.right)
        key=left+","+mid+","+right
        
        # Only if this is not a leaf node, store it!
        if root.left!=None or root.right!=None:
            self.dp[key]=self.dp.get(key,0)+1
        return key
    
    def dupSub(self, root):
        self.dp={}
        
        # Will just store the sub-trees in the dp dictionary
        self.dupRecur(root)
        # One liner for the below 4 lines of code
        return 1 if(max(self.dp.values())>=2) else 0
        # for i in self.dp.values():
        #     # if there's some sub-tree that occurred more than once
        #     if i>1:
        #         return 1
        # return 0