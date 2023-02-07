from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))
res = []

target = 1
while(len(q) != 0):
    if(target == k):
        res.append(str(q.popleft())) # 출력 시 join 활용 위해 str 타입으로 변경
        target = 1
    else:
        q.rotate(-1)
        target += 1

# 출력
print("<{0}>".format(', '.join(res)))