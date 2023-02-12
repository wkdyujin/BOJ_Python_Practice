n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    arr.sort() # O(nlogn)
    union = arr[0] + arr[1]
    arr[0], arr[1] = union, union
    
print(sum(arr))