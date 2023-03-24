def solution(s, skip, index):
    answer = ''
    arr = []
    for i in range(ord('a'), ord('z') + 1):
        if(chr(i) not in skip):
        	arr.append(chr(i))
    print(arr)
    
    for i in s:
        new_idx = (arr.index(i) + index) % len(arr)
        answer = answer + arr[new_idx]
    return answer