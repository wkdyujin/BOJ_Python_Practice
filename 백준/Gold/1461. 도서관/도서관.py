n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
res = 0

neg, pos = [], []
for num in nums:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

for i in range(0, len(neg), m):
    res += neg[i] * (-2)
for i in range(len(pos)-1, -1, -m):
    res += pos[i] * 2

if n > 1:
    res -= max(abs(nums[0]), abs(nums[-1]))
else:
    res -= nums[0]
print(res)