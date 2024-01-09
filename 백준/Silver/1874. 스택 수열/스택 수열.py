n = int(input())
res = []
stack = []
i = 1 # 다음 push될 수
enable = True

for _ in range(n):
    cur = int(input()) # 현재 pop되어야하는 수
    if i < cur:
        for _ in range(i, cur):
            stack.append(i)
            res.append('+')
            i += 1
        res.append('+')
        res.append('-')
        i += 1
    elif i == cur:
        res.append('+')
        res.append('-')
        i += 1
    else:
        while True:
            if not stack:
                enable = False
                break
            if stack[-1] < cur:
                enable = False
                break
            elif stack[-1] == cur:
                stack.pop()
                res.append('-')
                break
            else:
                stack.pop()
                res.append('-')

if enable:
    for item in res:
        print(item)
else:
    print('NO')