class Solution:
    def betterString(self, str1, str2):
        # Code here
        contris={}
        str1_count,str2_count=1,1
        
        for i in range(len(str1)):
            # the new contri of this ith char will be the len of the curr str part
            new_contri=str1_count*2
            # the new_contri will be affected if this char had arised before too, so will
            # subtract it's last contribution in the overall count of subsequences
            new_contri=new_contri-contris.get(str1[i],0)
            contris[str1[i]]=str1_count
            str1_count=new_contri
        
        contris={}
        # same for str2
        for i in range(len(str2)):
            new_contri=str2_count*2
            new_contri=new_contri-contris.get(str2[i],0)
            contris[str2[i]]=str2_count
            str2_count=new_contri
            
        return str1 if str1_count>str2_count else str2 if str2_count>str1_count else str1 