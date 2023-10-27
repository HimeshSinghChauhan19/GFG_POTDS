class Solution:
    def isPossible(self, N, arr):
        # code here
        # print(arr)
        rem=0
        for i in arr:
            num=("" if(rem==0) else str(rem)) + str(i)
            rem=int(num)%3
            # print(num)
        # print(rem)
        return 1 if(rem==0) else 0