import sys
input = sys.stdin.readline

arr = []
n = int(input())
friends = [0 for _ in range(n)]

for _ in range(n):
    arr.append(input())
    
for i in range(n):
    for j in range(n):
        if(i == j):
            continue
            
        if(arr[i][j] == 'Y'):
            friends[i] += 1
        else: # i, j가 친구가 아닐 때
            for k in range(n):
                if(arr[i][k] == 'Y' and arr[j][k] == 'Y'):
                    friends[i] += 1
                    break # 연결한 친구 있으면 더이상 찾지 않음
                    
print(max(friends))