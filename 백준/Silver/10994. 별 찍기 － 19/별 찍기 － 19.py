n = int(input())
width = 1 + 4 * (n - 1)
arr = [[' ' for _ in range(width)] for _ in range(width)]

def recursion(arr, n, start, end):
    if(n == 0):
        return arr
    
    for i in range(start, end + 1): #첫번째, 마지막번째
        arr[start][i] = arr[end][i] = '*'
        
    for i in range(start + 1, end): # 2 ~ (width-1)번째
        arr[i][start] = arr[i][end] = '*'
        
    return recursion(arr, n - 1, start + 2, end - 2)
    
for i in recursion(arr, n, 0, width - 1):
    print(''.join(i))