from itertools import permutations

n = int(input())
arr = list(map(int, input().split()))
p_list = set(permutations(arr, n))
max_res = 0

for p in p_list:
    res = 0
    for i in range(n - 1):
        res += abs(p[i + 1] - p[i])
    max_res = max(res, max_res)
    
print(max_res)