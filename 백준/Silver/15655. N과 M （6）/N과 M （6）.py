N, M= map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []

def back(start):
    if(len(stack) == M):
        print(' '.join(map(str, stack)))
        return
    
    for idx in range(start, len(arr)):
        if arr[idx] not in stack:
            stack.append(arr[idx])
            back(idx)
            stack.pop()
back(0)