# 문제: 2xn바닥을 채우는 경우의 수?
#       1x2 2x1 2x2의 덮개를 사용 

n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3,n+1):
    d[i] = (d[i-1] + 2*d[i-2])%796796 
print(d[n])