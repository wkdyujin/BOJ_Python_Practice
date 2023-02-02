arr = []
false1 = 0
false2 = 0

for _ in range(9):
    ans = int(input())
    arr.append(ans)

arr.sort()

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if(sum(arr) - (arr[i] + arr[j]) == 100):
            false1 = arr[i]
            false2 = arr[j]

for i in arr:
    if (i != false1 and i !=false2):
        print(i)