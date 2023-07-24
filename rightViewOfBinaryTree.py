'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        # print(root)
        # print(root.data,root.left,root.right)

        queue=[]
        queue.append(root)
        
        ans=[]
        
        while(len(queue)>0):
            n=len(queue)
            for i in range(n):
                
                node=queue.pop(0)
                # Will take only the rightmost elements of the level order traversal
                if(i==n-1):
                    ans.append(node.data)
                    
                if(node.left!=None):
                    queue.append(node.left)
                if(node.right!=None):
                    queue.append(node.right)
        # print(ans)
        return ans