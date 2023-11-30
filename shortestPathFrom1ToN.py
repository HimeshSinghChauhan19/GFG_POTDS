class Solution:
    def minimumStep (self, n):
        # final no. of steps
        steps=0
        
        # representing the current number
        curr=n
        while(curr>=1):
            if(curr%3==0):
                steps+=1
                curr//=3
            else:
                steps+=curr%3
                curr-=curr%3
            if(curr==1):
                return steps
            if(curr<3):
                return steps+1