# DefaultDict with 26 keys => frequency dict. Alphabetical order.
# For each str, construct dict and freeze it. 
# Return values
# O(nm); m is max length of a word, n is number of words
# Space is O(nm)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        def hashable_dict(d: dict) -> tuple:
            return tuple(sorted(d.items()))        
        
        for s in strs:
            freq_dict = defaultdict(int)
            for c in s:
                freq_dict[c] += 1
            res[hashable_dict(freq_dict)].append(s)
        
        print(res, res.values())
        return list(res.values())