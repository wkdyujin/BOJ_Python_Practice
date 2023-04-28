def solution(n, words):
    answer = [0, 0]
    user_word = set([words[0]])
    
    for i in range(1, len(words)):
        if (words[i-1][-1] != words[i][0]) or (words[i] in user_word):
            if (i+1) % n == 0:
                answer[0], answer[1] = n, (i+1) // n
            else:
                answer[0],answer[1] = (i+1) % n, (i+1) // n + 1
            break
        else:
            user_word.add(words[i])

    return answer