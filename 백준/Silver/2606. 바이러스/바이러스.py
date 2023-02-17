from collections import deque
import sys
input = sys.stdin.readline

com_n = int(input())
line = int(input())
arr = [[0] for _ in range(com_n + 1)]

for _ in range(line):
    com1, com2 = map(int, input().split())
    arr[com1].append(com2)
    arr[com2].append(com1)

res = -1 # 1 제외
queue = deque([1])

# print(arr)

while(len(queue) != 0):
    pop = queue.popleft()
    if(arr[pop][0] == 0):
        for i in range(1, len(arr[pop])):
            queue.append(arr[pop][i])
        res += 1
        arr[pop][0] = 1

print(res)