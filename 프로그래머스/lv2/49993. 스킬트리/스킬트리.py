def solution(skill, skill_trees):
    answer = 0
    stack = list(reversed(skill))
    
    for skills in skill_trees:
        s = stack.copy()
        
        for c in skills:
            if c in s:
                if c != s.pop():
                    break
        else:
            answer += 1
    
    return answer