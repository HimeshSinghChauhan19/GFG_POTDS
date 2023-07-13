from typing import List
from collections import Counter as CT

class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        '''
        Both of the ways of implementation work, it's just the way they are written
        Time: 0.09
        '''
        # Implementation 1
        # return len(dict(CT(arr)).values())==len(set(dict(CT(arr)).values()))
        
        # Implementation 2
        d1=dict(CT(arr))
        return len(d1.values())==len(set(d1.values()))