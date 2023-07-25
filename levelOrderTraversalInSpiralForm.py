#Function to return a list containing the level order traversal in spiral form.
def findSpiral(root):
    curr_queue=list()
    curr_queue.append(root)
    level_count=0
    ans=list()
    
    while(len(curr_queue)!=0):
        # print("This is the ",level_count,"th level.")
        n=len(curr_queue)
        
        if(level_count%2==0):
            # for even levels, right-to-left
            for i in range(n-1,-1,-1):
                ans.append(curr_queue[i].data)
        else:
            # for odd levels,left-to-right
            for i in range(0,n):
                ans.append(curr_queue[i].data)
        
        # Will just explore all the nodes in the curr_queue currently
        for _ in range(n):
            temp=curr_queue[0]
            # print(temp.data)
            curr_queue=curr_queue[1:]
            if(temp.left!=None):
                curr_queue.append(temp.left)
                
            if(temp.right!=None):
                curr_queue.append(temp.right)
        
            
        level_count+=1
        
    return ans