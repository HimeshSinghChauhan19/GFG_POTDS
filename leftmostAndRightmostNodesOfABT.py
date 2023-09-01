def printCorner(root):
    
    # print corner data, no need to print new line
    # code here
    queue=list()
    queue.append(root)
    while(len(queue)!=0):
        size=len(queue)
        print(queue[0].data,end=" ")
        if(size!=1):
            print(queue[size-1].data,end=" ")
            
        for i in range(size):
            node=queue.pop(0)
            # print(node.data)
            if(node.left!=None):
                queue.append(node.left)
            if(node.right!=None):
                queue.append(node.right)