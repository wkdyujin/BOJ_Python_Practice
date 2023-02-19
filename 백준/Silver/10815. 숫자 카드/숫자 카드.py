n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

def binary_sort(low, high, target):
    mid = (low + high) // 2
    if(n_list[mid] == target):
        return 1
    if(low > high):
        return 0
    if(n_list[mid] > target): # 더 작을 때
        return binary_sort(low, mid - 1, target)
    else: # 클 때
        return binary_sort(mid + 1, high, target)
        
for target in m_list:
    print(binary_sort(0, n - 1, target), end = ' ')