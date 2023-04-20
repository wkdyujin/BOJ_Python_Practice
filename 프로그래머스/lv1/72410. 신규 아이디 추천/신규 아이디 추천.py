def solution(new_id):
    answer = ''
    #1
    new_id = new_id.lower()
    #2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-','_','.']:
            answer += c            
    #3
    while '..' in answer:
        answer = answer.replace('..', '.')    
    #4
    answer = answer.strip('.')
    #5
    if answer == '':
        answer = 'a'
    #6
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.strip('.')
    #7
    if len(answer) < 3:
        answer += (3 - len(answer))*answer[-1]
    print(answer)
    return answer