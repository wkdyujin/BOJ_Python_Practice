# stack

def solution(s):
    answer = True
    stack = []
    
    for c in s:
        if c == '(':
            stack.append(c)
            
        if c == ')':
            if not stack:
                print("ㄴㄴ")
                answer = False
                break
            stack.pop()
            
    if stack:
        answer = False
                
    return answer