class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        itr2=n//2
        itr1=0
        mx=max(arr)+1
        for i in range(n):
            if(i%2==0):
                # arr[i]=new_elem*mx+original_elem
                arr[i]=(arr[itr1]%mx)*mx+(arr[i]%mx)
                itr1+=1
            else:
                arr[i]=(arr[itr2]%mx)*mx+(arr[i]%mx)
                itr2+=1
        for i in range(n):
            arr[i]//=mx
        # print(arr)