from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if strs == [""]:
            return [[""]]
        
        temp = [ []*i for i in range(len(strs))]
        counts = []
        result = []
        
        for word in strs:
            count = Counter(word)
            if count not in counts:
                counts.append(count)
                idx = counts.index(count)
                temp[idx].append(word)
            else:
                idx = counts.index(count)
                temp[idx].append(word)


        for arr in temp:
            if len(arr) != 0:
                result.append(arr)
        
        return result