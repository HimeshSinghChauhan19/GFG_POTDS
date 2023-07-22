"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def reverse(self,head, k):
        temp=head
        prevGroupElem1=None
        prevGroupElem2=None
        # newHead=None
        first=True
        
        while(temp!=None):
            # print(temp.data)
            # temp=temp.next
            
            # Do the below steps before starting of every group  
            if(prevGroupElem1==None):
                # just for the 1st time update the prevGroupElem1, otherwise everytime 
                # update the prevGroupElem2 further
                # print("First group and so setting prevGroupElem1 to this, that is ",temp.data)
                prevGroupElem1=temp
                # prevGroupElem1.next=None
                # if(temp==None):
                    # print("HERE WE HAD A NONE VALUE!")
                # prevGroupElem1.next=None
            else:
                # print("Setting prevGroupElem2 to",temp.data)
                # prevGroupElem1.next=temp
                # prevGroupElem1=temp
                prevGroupElem2=temp
                # prevGroupElem1.next=None
            
            count=1
            
            prevNode=None
            # go for every group, one by one
            while(count<=k):
                if(temp==None):
                    # print("Temp became None in between the group counting")
                    # print("Count was",count)
                    return head
                # Saving the next node of the current node for later usage
                nextTempNode=temp.next
                temp.next=None
                # print("Here next node is",nextTempNode.data if(nextTempNode!=None) else "(Next node is None!)")
                
                if(prevNode==None):
                    # for the 1st elem of every group, just update the prevNode, that's it
                    # print("Setting prevNode for first time in this group, to",temp.data)
                    prevNode=temp
                else:
                    # Means we gotta connect this temp node to that node
                    # and also update the temp node to the next node after this one
                    
                    temp.next=prevNode
                    # print("Setting the prevNode to",temp.data)
                    prevNode=temp
                    
                    
                if(count==k):
                    # If we are at the last element
                    if(first!=True):
                        # will have to make the prevGroupElem1 point to this node
                        prevGroupElem1.next=temp
                        
                        # and will also update the prevGroupElem1 to now the 
                        # prevGroupElem2, so that the next new elem in a 
                        # new group can be kept in the prevGroupElem2
                        prevGroupElem1=prevGroupElem2
                        # print("This wasn't first group")
                        pass
                    if(first==True):
                        # newHead=temp
                        # print("This was 1st group...setting the head to this node, that is",temp.data)
                        head=temp
                        first=False
                    
                    temp=nextTempNode
                    # print("This was group ",count)
                    # Means this group has been done and finished
                    break
                
                if(nextTempNode==None):
                    # If we won't have a next elem, then just update
                    prevGroupElem1.next=temp
                temp=nextTempNode
                
                count+=1
        # prevGroupElem1.next=None
        return head