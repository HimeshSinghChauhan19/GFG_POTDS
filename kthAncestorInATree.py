def checkChild(parent,child,kVal):
    ''' 
        Will just check for a node if it has a child 
        down k levels with the value child
    '''
    if(parent==None):
        return False
        
    if(kVal<0 or (kVal==0 and parent.data!=child)):
        return False
    
    
    if(parent.data==child and kVal==0):
        return True
        
    # Can compact this whole if thing below to a 1 liner return statement,
    # but for better visibility and understand even this is fine
    
    if(checkChild(parent.left,child,kVal-1)==True):
        return True
    
    if(checkChild(parent.right,child,kVal-1)==True):
        return True
    
    return False

def kthAncestor(root,k, child):
    queue=[]
    queue.append(root)
    count=0
    # will contain the nodes at various levels of the tree starting
    # from 0 to the last
    tree_levels=[]
    
    while(len(queue)!=0):
        n=len(queue)
        temp_level=[]
        
        for i in range(n):
            node=queue[0]
            temp_level.append(node)
            queue.pop(0)
            # print("Currently the node is",node.data)
            
            if(node.data==child):
                if(count-k<0):
                    # if the level of the parent is <0 means it is invalid
                    return -1
                    
                # print("This is the node whose kth parent we need:",child)
                # print("The parent will be at level:",count-k)
                # print("The nodes at the level where parent will be present are:",end=" ")
                # print(tree_levels[count-k])
                # So will just try every parent node at the level count-k
                # to check which parent belongs to the child in this func
                for parent in tree_levels[count-k]:
                    # print("True Returned",parent.data) if(checkChild(parent,child,k) \
                    # ==True) else None    
                    if(checkChild(parent,child,k)==True):
                        return parent.data
                        
            if(node.left!=None):
                queue.append(node.left)
            
            if(node.right!=None):
                queue.append(node.right)
                
        # Add the nodes of this level(count'th level)
        tree_levels.append(temp_level)
        count+=1     
        
        
    # print("Finally returning -1 bcz there was no valid parent found in the tree")
    return -1