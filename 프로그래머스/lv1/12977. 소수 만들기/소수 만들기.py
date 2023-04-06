from itertools import combinations

def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
        
def solution(nums):
    answer = 0
    comb_arr = list(combinations(nums, 3))
    
    for arr in comb_arr:
        if(isPrime(sum(arr))):
            answer += 1

    return answer