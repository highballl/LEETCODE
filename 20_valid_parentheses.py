class Solution:
    def isValid(self, s: str):
        s = list(s) # 받아온 문자열 리스트로 만들기
        stack = [] # 빈 스택
        table = { # 괄호 - 딕셔너리
            "(": ")",
            "{": "}",
            "[": "]"
        }
        
        # ()
        keys = table.keys()
        stack.append(s.pop())  # 최초에 문자열 제일 오른쪽의 괄호를 스택에 넣고 시작
        while s:
            r = stack[-1]  #")"
            l = s.pop()  #"("
            
            if l in keys and table[l] == r:
                stack.pop()
                if not stack:
                    return True
                continue
            else:  # (((){)
                stack.append(l)
        
        return False
           
        
       

#s = "()[]"
#s = "{[]}"
#s = "([)]"
#s = "(]"
print(Solution().isValid(s))
        