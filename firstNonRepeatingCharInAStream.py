from collections import OrderedDict
class Solution:
    def FirstNonRepeating(self, A):
        nonRepChars=OrderedDict()
        ans = ""

        '''
        The dict will be of the form: {char1:validOrNot,char2:validOrNot,char3:...}
        here validOrNot refers if the char is non-repeating or not
        '''
        for ch in A:
            try:
                # If the elem is in the dict, then now will not be anymore
                temp=nonRepChars[ch]
                # 0 here means that now the elem is not repeating anymore 
                nonRepChars[ch]=0
                
                # if(ch not in nonRepChars):
                #     add it in that
            except Exception as e:
                # when the elem is not in the dic so means it will be considered as
                # repeating char
                nonRepChars[ch]=1
                
                # if there already means it came for the second time, so now it's not 
                # non-repeating anymore so mark it as done, means value 0
            
            # Everytime getting the 1st elem from the list of non-repeating chars
            # print(f"Checking for a valid char... in the dict: {nonRepChars}")
            for char,isValid in nonRepChars.items():
                if(isValid==1):
                    ans+=char
                    break
            else:
                # When we don't have any non-repeating char available
                # so will append a # sign to the ans var
                ans+='#'
            # keep adding the chars to the ans string while all this
        return ans