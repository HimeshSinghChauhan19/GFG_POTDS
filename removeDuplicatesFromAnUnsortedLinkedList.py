'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        temp=head
        checkDuplis=dict()
        prevNode=None
        
        while(temp!=None):
            try:
                tempVar=checkDuplis[temp.data]
                # If we will be here, means this temp.data has came for the 2nd time
                # in the linked list, so will just remove it now
                
                prevNode.next=temp.next
                # then saying that just go to the next node now, no need to store
                # this node as the prevNode, because we are not including this in the
                # linked list
                temp=temp.next
                continue
            
            except Exception as e:
                # if this data has came for the 1st time, so make it a key,
                # so that for the next time, this won't be included
                checkDuplis[temp.data]=1
            # Storing the prevNode to use in the removal of the next node
            prevNode=temp
            temp=temp.next
        return head