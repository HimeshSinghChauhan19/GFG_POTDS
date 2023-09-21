class Solution:
    def countWays(self, steps):
        #Base cases
        if steps < 3:
            return steps
       
        #Initialize variables
        prev_step, curr_step, next_step, modulo = 1, 1, 2, 10**9 + 7
       
        #Calculate the number of ways iteratively
        for i in range(3, steps + 1):
            prev_step, curr_step, next_step = curr_step, next_step, (prev_step + curr_step + next_step) % modulo
       
        #The 'next_step' variable now holds the count of ways to reach the top
        return next_step