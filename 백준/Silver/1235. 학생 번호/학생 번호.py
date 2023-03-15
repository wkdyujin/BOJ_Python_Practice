n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

for i in range(1, len(arr[0])+1):
    if(len(set([num[-i:] for num in arr])) == n):
        print(i)
        break