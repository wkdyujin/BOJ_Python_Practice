room_num = str(input())
arr = []
result = 0

for i in range(10):
    arr.append(room_num.count(str(i)))

sixnine = (arr[6] + arr[9] + 1) // 2
arr[6], arr[9] = 0, 0

if (max(arr) < sixnine):
    print(sixnine)
else:
    print(max(arr))