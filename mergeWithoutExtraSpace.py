class Solution:
    
    def merge(self,arr1,arr2,n,m):

        # del arr1[:]
        # temp = sorted(list(set(arr2).union(set(arr1))))
        temp=sorted(arr1+arr2)
        
        # temp=[1,1,1,1]
        # print(temp)
        # temp=sorted(arr1)
        del arr1[:]
        del arr2[:]
        arr1+=temp[:n]
        arr2+=temp[n:]
        # print(arr1)
        # print(arr2)
        
        # arr1=list(set(arr1))
        # del arr1[:]
        # # arr1.sort()
        # arr1+=temp