from collections import OrderedDict as OD
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        
        temp=head
        # print(type(temp.data))
        d1=OD()
        d1[0]=0
        d1[1]=0
        d1[2]=0
        while(temp!=None):
            # print(temp.data)
            # just simply getting the frequency of the data elements
            d1[temp.data]+=1
            temp=temp.next
        
        temp=head
        
        while(temp!=None):
            if(d1[0]!=0):
                temp.data=0
                d1[0]-=1
            elif(d1[1]!=0):
                temp.data=1
                d1[1]-=1
            else:
                temp.data=2
                d1[2]-=1
            temp=temp.next
            
        return head