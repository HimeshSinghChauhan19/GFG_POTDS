class Solution:
    def maxEqualSum(self, N1:int,N2:int,N3:int, S1 : List[int], S2 : List[int], S3 : List[int]) -> int:
        # code here
        ls1=[S1,S2,S3]
        ls2=[N1,N2,N3]
        ls=[sum(S1),sum(S2),sum(S3)]
        minSum=min(ls)
        if(ls[0]==ls[1]==ls[2]):
            return ls[0]
        '''
        Updation: Instead of making changes in the ls1 lists, removing the 0th elems again and again,
                  trying to just use iterators for the 3 stacks
        '''
        # Will keep increment in these, instead of removing the 0th elems from the lists, 
        # cause removing elems and updating the lists is quite a time consuming task, of slicing
        iterators=[0,0,0]
        for i in range(9999999):
            for j in range(3):
                if(ls[j]>minSum):
                    
                    '''
                    The commented code was part of the previous logic where slice operator was 
                    used to remove the 0th elem of the lists
                    '''
                    # ls[j]-=ls1[j][0]
                    ls[j]-=ls1[j][iterators[j]]
                    # If condition satisfied, then do the needful ;)
                    if(ls[0]==ls[1]==ls[2]):
                        return ls[0]
                    # If I have to increment the iterator to (len of that list)-1 means it
                    # is fully empty now and hence return 0
                    if(iterators[j]==(ls2[j]-1)):
                        return 0
                    # Else just increment the iterator to next position on the jth list
                    iterators[j]+=1
                    # I was finding the len everytime too, such a dumb move to throw so many O(n)'s
                    # if(len(ls1[j])==1):
                        # Means cannot do anything after this better than 0
                        # Also if this was the case then the slicing line would have created a problem 
                        # return 0
                    # Else remove the first elem of the array
                    # This below line was taking O(n) TC everytime it was called
                    # ls1[j]=ls1[j][1:]
                    
                minSum=min(ls)