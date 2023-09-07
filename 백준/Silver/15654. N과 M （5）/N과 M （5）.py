N, M = map(int, input().split())
arr = list(map(int, input().split()))
stack = []
arr.sort()

def back():
    if len(stack) == M:
        print(' '.join(map(str, stack)))
        return
    for i in arr:
        if i not in stack:
            stack.append(i)
            back()
            stack.pop()
            
back()