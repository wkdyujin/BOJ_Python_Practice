def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
        
        
def solution(nums):
    answer = 0
    n = len(nums)
    r = 3
    arr = [0] * r
    comb_arr = [] # 결과 배열
    
    def combination(level, idx): # nCr
        if(level == r):
            comb_arr.append(arr.copy())
            return

        for i in range(idx, n):
            arr[level] = nums[i]
            combination(level + 1, i + 1)
    
    # 조합 생성
    combination(0, 0)
    
    # 소수 판별
    for arr in comb_arr:
        if(isPrime(sum(arr))):
            answer += 1

    return answer