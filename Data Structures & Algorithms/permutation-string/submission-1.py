# Cannot do a set bc it means no repeated chars.
# Instead do a freq dict.
# Construct freq dict of s1. 
# Then do sliding window. If i in freq_dict, begin constructing new freq_dict_candidate
# Move j. If j not in freq_dict or the resulting count exceeds the freq_dict, move i to j.
# Or rather.. have an end point at i + len(s1) away. freq_dict_candidate must be equal to freq_dict

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Construct freq_dict
        freq_dict = defaultdict(int)
        for c in s1:
            freq_dict[c] += 1
        print(freq_dict)

        index = 0 # Sliding window
        while index <= len(s2) - len(s1):
            freq_dict_candidate = defaultdict(int)
            for i in range(index, index + len(s1)):
                char = s2[i]
                amt_seen = freq_dict_candidate[char]
                if char in freq_dict and amt_seen < freq_dict[char]:
                    freq_dict_candidate[char] += 1
                else:
                    index += 1
                    break
            print(freq_dict_candidate, index)
            if freq_dict == freq_dict_candidate:
                return True
            # else: # early return to debug
                
            #     return False
        return False                