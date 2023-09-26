class Solution:
    def fourSum(self, arr, k):
        # code here
        n=len(arr)
        arr.sort()
        ans=set()
        
        for i in range(n):
            for j in range(i+1,n):
                curr_sum=arr[i]+arr[j]
                # if the summation of the first 2 elems is only >= k, then there is no chance of getting any result now,
                # if(curr_sum>=k):
                #     return ans
                    
                # will use the 2 pointer approach in the next 2 elems, giving a O(n) time complexity over the n^2 that is already being given
                # by the upper 2 loops
                left,right=j+1,n-1
                left_sum=k-curr_sum
                # print("left sum is ",left_sum)
                while(left<right):
                    if( (arr[left]+arr[right]) < left_sum ):
                        left+=1
                        continue
                    
                    if( (arr[left]+arr[right]) > left_sum ):
                        right-=1
                        continue
                    
                    if(arr[left]+arr[right]==left_sum):
                        # print([arr[i],arr[j],arr[left],arr[right]])
                        ans.add((arr[i],arr[j],arr[left],arr[right]))
                        left+=1
                        right-=1
        ans=sorted(list(ans))
        return ans
        ''' 
        Dropped this idea, cause the tuples needed should be
        unique, so that makes the things a little easier
        '''
        #     # will find the frequencies of these elems that have given
        #     # us the summation, cause they can be more and so will 
        #     # consider all the possibilities, 
        #     # it will be like a*b, where a,b are the freqs
        #     for i1 in range(left,n):
        #         if(arr[i1]==arr[left]):
        #             left_freq+=1
                    
        #     for j1 in range(right,-1,-1):
        #         if(arr[j1]==arr[right]):
        #             right_freq+=1
            # so total combinations will be left_freq*right_freq
                  