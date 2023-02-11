n, m = map(int, input().split()) # 3, 5
arr = [[] for _ in range(n)] # [[],[],[]]

for i in range(n):
    nums = input()
    for j in range(len(nums)):
        arr[i].append(int(nums[j]))

width = min(n, m)

def find(width, arr):
    for i in range(len(arr) - width + 1):
        for j in range(len(arr[0]) - width + 1):
            if(width == 1):
                return 1
            if(arr[i][j] == arr[i][j+width-1] == arr[i+width-1][j] == arr[i+width-1][j+width-1]):
                return width * width
                
    return find(width - 1, arr) # 위에서 return 없었을 시

print(find(width, arr))