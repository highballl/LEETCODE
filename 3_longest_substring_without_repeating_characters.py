from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = defaultdict()
        max_cnt = 0
        count = 0
        idx = 0
        idx_next = 0
        
        while idx < len(s):
            if s[idx] == ' ':
                key = '_'
            key = s[idx]
            try:
                if visited[key]:
                    if count > max_cnt:
                        max_cnt = count
                    visited = defaultdict()
                    count = 0
                    idx = 0 + idx_next
                    idx_next += 1
                    continue
            except:
                visited[key] = True
                count += 1  
                idx += 1
                if count > max_cnt:
                        max_cnt = count

        return max_cnt
