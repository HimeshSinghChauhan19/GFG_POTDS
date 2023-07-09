class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        # temp=list()
        # for i in range(n):
        #     temporary=list()
        #     for j in range(n):
        #         if(j==i):
        #             continue
        #         temporary.append(arr[i]+arr[j])
        #     temp.append(temporary)
        
        # itr=0
        # for j in range(n):
        #     for i in range(n):
        #         if(i==j):
        #             continue
        #         else:
        #             if(arr[i]+temp[i])
        # print(temp)
        
        # The code would work without this line too...
        # if(n<3 or (n==3 and (arr[0]+arr[1]+arr[2])!=0)):
        #     return 0
        arr.sort()
        for i in range(n):
            it1=i+1
            it2=n-1
            while(it1<it2):
                summation=arr[i]+arr[it1]+arr[it2]
                if(summation>0):
                    it2-=1
                elif(summation<0):
                    it1+=1
                else:
                    return 1
        return 0