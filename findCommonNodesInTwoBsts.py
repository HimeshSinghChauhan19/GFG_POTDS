class Solution:
    def inOrder(self,root,st):
        if(root!=None):
            self.inOrder(root.left,st)
            st.add(root.data)
            self.inOrder(root.right,st)
            
    #Function to find the nodes that are common in both BST.
    def findCommon(self, root1, root2):
        # code here
        st1=set()
        st2=set()
        # Just traverse through both BSTs and get the elements in sets
        self.inOrder(root1,st1)
        self.inOrder(root2,st2)
        
        # Just return the sorted list of common intersecting elements 
        return sorted(st1.intersection(st2))