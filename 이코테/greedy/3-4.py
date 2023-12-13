# 문제: 어떠한 수를 1로 만들기 최소 횟수를 구해라!
#       (1을 빼거나 k를 나누기만 가능, k로 나누어 떨어질때만 나누기 가능) 
# 풀이 방법 : n이 1이 될때까지 나누기가 가능한 경우라면 나누기를 우선으로 진행한다. 

n,k = map(int,input().split())
count = 0
while n>1:
    if n%k == 0:
        n = n//k
        count += 1
    else:
        n -= 1
        count +=1
print(count)
