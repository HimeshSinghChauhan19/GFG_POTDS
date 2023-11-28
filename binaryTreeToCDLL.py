'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

ls=[]
class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        global ls
        ls=[]
        def inord(root):
            global ls
            if(root!=None):
                inord(root.left)
                ls.append(root.data)
                inord(root.right)
            
            
        class node_in_ll:
            def __init__(self,data):
                self.data=data
                self.left=None
                self.right=None
        
        inord(root)
        
        # ans=node_in_ll(23) 
        # ans2=node_in_ll(34)
        # ans2.left=ans
        # ans.right=ans2
        # ans2.right=ans
        # ans.left=ans2
        
        main_ans=node_in_ll(ls[0])
        
        new_ls=[]
        new_ls.append(main_ans)
        for i in range(1,len(ls)):
            
            new_ls.append(node_in_ll(ls[i]))
            new_ls[i-1].right=new_ls[i]
            new_ls[i].left=new_ls[i-1]
        new_ls[0].left=new_ls[-1]
        new_ls[-1].right=new_ls[0]
        
        # print(new_ls)
        # print(ls)
        # print(ans)
        return new_ls[0]