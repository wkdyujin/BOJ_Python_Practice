import copy

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
res_max, res_min = -100000000000, 100000000000

def back(op_list):
    global res_max
    global res_min
    if(len(op_list) == N-1):
        copy_nums = copy.deepcopy(nums)
        for i in range(N-1):
            copy_nums[i+1] = cal(copy_nums[i], copy_nums[i+1], op_list[i])
        res_max = max(res_max, copy_nums[-1])
        res_min = min(res_min, copy_nums[-1])
            
    else:
        for i in range(4):
            if(ops[i] - op_list.count(i) != 0):
                op_list.append(i)
                back(op_list)
                op_list.pop()

def cal(n1, n2, op):
    if(op == 0):
        return n1 + n2
    if(op == 1):
        return n1 - n2
    if(op == 2):
        return n1 * n2
    if(op == 3 ):
        if(n1 < 0):
            return n1*(-1)//n2 * (-1)
        else:
            return n1//n2
        
back([])
print(res_max, res_min)