n = int(input())
question = input()
stack = []
nums = []
op = ['+', '-', '*', '/']
res = ''

for i in range(n):
    nums.append(int(input()))

for i in range(len(question)):
    if (question[i] in op):
        # 연산자일 때 => stack pop
        two, one = stack.pop(), stack.pop()
        res = '(' + str(one) + question[i] + str(two) + ')'
        stack.append(res)
    else:
        # 문자일 때 => stack push
        stack.append(question[i])
        
i = 0
for eng in range(ord('A'), ord('A') + n):
    res = res.replace(chr(eng), str(nums[i]))
    i += 1

print("{:.2f}".format(eval(res)))