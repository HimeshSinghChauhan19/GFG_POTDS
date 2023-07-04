class Solution:

        def maxIndexDiff(self,arr, n):

            min_elems = [0] * n
            max_elems = [0] * n

            min_elems[0] = arr[0]
            max_elems[n - 1] = arr[n - 1]

            # Getting the min & max elems for the indices, the logic is that
            # this will give me the minimum possible elem for indices, say 0,1,2,..
            # and max_elems will give me the max elems till indices, say 0,1,2,...

            for i in range(1, n):
                min_elems[i] = min(min_elems[i - 1], arr[i])
                max_elems[n - i - 1] = max(max_elems[n - i], arr[n - i - 1])

            result = 0
            i = 0
            j = 0

            # While we get to any extreme position, means there is no possibilty 
            # for any better solution than this
            while(i < n and j < n):
                # if elem is <= means will try to look for further indices if they
                # are also giving me this condition true
                if(min_elems[i] <= max_elems[j]):
                    result = max(result, j - i)
                    j += 1
                else:
                    # if the ith elem is now greater than jth index and further 
                    # elems, so it is of no use for consideration now
                    i += 1
                    
            return result
