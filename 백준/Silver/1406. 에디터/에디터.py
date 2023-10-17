import sys
input = sys.stdin.readline

string = input().rstrip()
n = int(input())

s1 = list(string)
s2 = []

for _ in range(n):
    c = input().rstrip()
    if c[0] == 'L' and s1:
        s2.append(s1.pop())
        
    if c[0] == 'D' and s2:
        s1.append(s2.pop())
        
    if c[0] == 'B' and s1:
        s1.pop()
        
    if c[0] == 'P':
        s1.append(c[-1])
        
print(''.join(s1 + s2[::-1]))