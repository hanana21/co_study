# 3-4 책 풀이
# 풀이방법: 나누기를 우선적으로 하지만 n이 k보다 클때와 아닐 때를 구분한다. 

n,k = map(int,input().split())
count = 0
while n >= k: # n이 k보다 클때는 나누기 우선 
    while n%k !=0: # n이 k로 나누어지지 않을 때
        n -= 1
        count += 1
    n //= k
    count += 1
while n > 1: #n이 k보다 작을 때는 n이 1이 되기 전까지 1만 빼준다.
    n -= 1
    count += 1

print(count)