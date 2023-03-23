from itertools import combinations # 중복 허용 X, 순서 의미 X
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')

for i in range(1, n + 1):
    com = list(combinations(arr, i))
    
    for j in com:
        sour, soy = 1, 0
        for k in j:
            sour *= k[0]
            soy += k[1]
        res = min(res, abs(sour-soy))
    
print(res)