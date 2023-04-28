def solution(skill, skill_trees):
    answer = 0
    
    stack = []
    for i in range(len(skill)-1, -1, -1):
        stack.append(skill[i])
    print("스택:", stack)
    
    for skills in skill_trees:
        s = stack.copy()
        enable = True
        for c in skills:
            if c in s:
                if c == s[-1]:
                    s.pop()
                else:
                    enable = False
                    break
        if enable:
            answer += 1
    
    return answer