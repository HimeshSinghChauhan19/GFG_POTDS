#User function Template for python3

class Solution:
    def shortestCommonSupersequence(self, str1, str2, len_str1, len_str2):
        dp = [[-1 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

        for i in range(len_str1 + 1):
            for j in range(len_str2 + 1):
                if not i or not j:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + dp[i - 1][j - 1] if str1[i - 1] == str2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

        return len_str1 + len_str2 - dp[len_str1][len_str2]
        
        # commons=[]
        # prev_pos=0
        # for i in range(m):
        #     for j in range(prev_pos,n):
        #         if(X[i]==Y[j]):
        #             commons.append([i,j])    
        #             # the position of this elem will be the starting pos to search for the similar
        #             # elem in Y string
        #             prev_pos=j+1
        #             break
        # # print(commons)
        # ans=""
        # prev_ind1,prev_ind2=0,0
        
        # for i,j in commons:
        #     for it in range(prev_ind1,i):
        #         ans+=X[it]    
                
        #     for it in range(prev_ind2,j):
        #         ans+=Y[it]
        #     ans+=X[i]
        #     prev_ind1=i+1
        #     prev_ind2=j+1
            