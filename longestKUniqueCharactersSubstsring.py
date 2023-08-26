class Solution:

    def longestKSubstr(self, s, k):
        ''' Basicaly based on the sliding window technique(just a fancy name, otherwise u can get this on ur own too '''
        max_count=-1
        no_of_unique_chars=0
        # will contain the unique characters
        unique_chars=[]
        # the current size of the substring that is being considered
        total_count=0
        # will use this to slide the window to the right,
        left_iter=0
        # will use this to maintain the freq of the chars in the group, was the ultimate idea that took me around 30 mins to think about
        dp=[0]*26
        
        for i in range(len(s)):
            # will be increased everytime
            total_count+=1
                
            if(s[i] in unique_chars):
                # increase the freq of the char, note here the ord(s[i]) is getting the ascii of the char and -97 means we are getting the index
                # val for that char, like for a will be 0 (bcz 97-97), and for z will be 25 (bcz 122-97)
                dp[ord(s[i])-97]+=1
                pass
            else:
                dp[ord(s[i])-97]+=1
                unique_chars.append(s[i])
                no_of_unique_chars+=1
            
            # If currently there are k number of unique elements in total
            if(no_of_unique_chars==k):
                # compare the curr_count with max_count
                if(total_count>max_count):
                    max_count=total_count
                    
            elif(no_of_unique_chars<k):
                pass
            
            else:
                # have to remove the iter elem and see if the unique elem count 
                # is decreased?
                # checking if freq of the current(left_iter'th) elem
                while(True):
                    dp[ord(s[left_iter])-97]-=1
                    if(dp[ord(s[left_iter])-97]==0):
                        no_of_unique_chars-=1
                        # bcz the freq of this char has become 0 so, removing this from unique_chars
                        unique_chars.remove(s[left_iter])
                        left_iter+=1
                        total_count-=1
                        break
                    
                    total_count-=1
                    left_iter+=1
                    
                ''' 
                Trying to maintain the frequency of the chars in the right side, like; a,b,e,a,b,e,c,a for first 'a' the freq at right is 2.
                    This below logic was a bad try because it didn't consider the fact that the freq in the right side won't just consider the 
                    freq of the char in the group(suppose group as (a,b,e,a,b), rather it would consider the char that is already removed from 
                    the currrent group being considered.
                    
                '''
                # while(left_iter<len(s) and freq[left_iter]!=1):
                #     left_iter+=1
                #     total_count-=1
                    
                #     # if(left_iter>=len(s)):
                #     #     return max_count
                # if(left_iter>=len(s)):
                #     return max_count
                # # freq=1 means that this char was last and is not present in right side
                # # ignoring the lem that has freq 1, means no_of_uniqueChars-1
                # # will remove this char from unique_chars array
                # if(s[left_iter] in unique_chars):
                #     unique_chars.remove(s[left_iter])
                # else:
                #     # pass
                #     print(unique_chars)
                #     print("Here",s[left_iter])
                # left_iter+=1
                # total_count-=1
                # no_of_unique_chars-=1
                # then will keep on removing the chars from the left side till 
                # the len of unique chars in total becomes k
                # while(len(set(chars))!=k):
                #     chars.pop(0)      
                # no_of_unique_chars=len(set(chars))
                
                
        return max_count