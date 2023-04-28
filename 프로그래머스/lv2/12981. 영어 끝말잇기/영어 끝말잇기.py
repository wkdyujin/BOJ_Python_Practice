def solution(n, words):
    answer = [0, 0]
    word_list = set()
    word_list.add(words[0])
    
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in word_list:
            if (i+1) % n == 0:
                answer[0] = n
                answer[1] = (i+1) // n
            else:
                answer[0] = (i+1) % n
                answer[1] = (i+1) // n + 1
            break
        else:
            word_list.add(words[i])

    return answer