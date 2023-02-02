# 11721: 열 개씩 끊어 출력하기

# 문자열 길이에서 일의자릿수 떼고 반복문 돌려서 10글자씩 출력
# 반복문 끝나면 나머지 출력

string = input()

n = len(string) // 10

for i in range(1, n+1):
    print(string[(i-1)*10:i*10])
    
print(string[n*10:])