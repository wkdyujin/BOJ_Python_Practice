n = int(input())
if(len(str(n)) <= 2): # 2자릿수 (= 모두 한수)
    print(n)
elif(len(str(n)) == 3): # 3자리수
    res = 99
    while(n > 99):
        s = str(n)
        if(int(s[2]) - int(s[1]) == int(s[1]) - int(s[0])):
            res += 1
        n -= 1
    print(res)
        
else: # 1000
    print(144)