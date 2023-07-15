class Solution:
    
    #Function to delete middle element of a stack.
    def deleteMid(self, s, sizeOfStack):
        # Note that the ind is based on 1-based indexing, so will convert to
        # 0-based indexing later while accessing the numbers
        
        indToBeDeleted = (sizeOfStack+1)//2
        # print(type(s))
        # print(s)
        # print("Ind to be deleted: ",indToBeDeleted)
        
        # here the ind(0-based) to be deleted will be indToBeDeleted-1
        temp=s[:indToBeDeleted-1]+s[indToBeDeleted:]
        s.clear()
        # Changing the list inplace
        s+=temp