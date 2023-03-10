from itertools import product # 중복 조합 라이브러리 사용

a = list(product(['A','E','I','O','U'], repeat=5))
b = list(product(['A','E','I','O','U'], repeat=4))
c = list(product(['A','E','I','O','U'], repeat=3))
d = list(product(['A','E','I','O','U'], repeat=2))
e = list(product(['A','E','I','O','U'], repeat=1))
res = sorted(a+b+c+d+e)

def solution(word):
    target = tuple(word)
    answer = res.index(target) + 1
    
    return answer