N, M = map(int, input().split())
stack = []

def back(start):
    for i in range(start, N + 1):
        if(len(stack) == M):
            print(*stack)
            return
        
        if(i not in stack):
            stack.append(i)
            back(i)
            stack.pop()
            
back(1)