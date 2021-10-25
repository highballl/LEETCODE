from collections import defaultdict, deque
s = "cbacdcbc"

class Solution:
    def removeDuplicateLetters(self, s: str):

        # s에 있는 문자들을 딕셔너리화

        dict = defaultdict(int)
        visited = defaultdict(bool)
        for string in s:
            dict[string] += 1
            #visited[string] = False

        # dict = {
        #     "c": 2,
        #     "b": 1,
        #     "a": 1,
        #     "d": 

        # }
        
        s = deque(s)
        du = []
        not_du = []
        while s:
            temp = s.popleft()
            if dict[temp] > 1 and temp not in du:
                du.append(temp)
            elif temp not in not_du:
                not_du.append(temp)    
        
        answer = ''.join(s)
        return answer


print(Solution().removeDuplicateLetters(s))