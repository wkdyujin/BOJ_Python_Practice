import sys
input = sys.stdin.readline

n = int(input())
times = []
for i in range(n):
    start, end = map(int, input().split())
    times.append([start, end])

# 종료 시간 기준 정렬
times.sort(key = lambda x: (x[1], x[0]))

cur_e = times[0][1] # 종료
res = 1

for i in range(1, n):
    if times[i][0] >= cur_e:
        cur_e = times[i][1]
        res += 1

print(res)