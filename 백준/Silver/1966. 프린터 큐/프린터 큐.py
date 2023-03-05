from _collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque([])

    for i in range(len(arr)):
        q.append([arr[i], i]) # -> q[0][0]: 중요도 / q[0][1]: 문서번호

    cnt = 0
    target = q[m][1] # 궁금한 문서 번호

    while(True):
        if(q[0][0] == max(q)[0]):
            cnt += 1
            if(q[0][1] == target):
                break
            q.popleft()
        else:
            q.rotate(-1)

    print(cnt)