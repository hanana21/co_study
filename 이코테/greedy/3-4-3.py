# 3-4 책 풀이 
# 푸는 방법: n이 k보다 작아질때 까지 나눈 몫은 n에 저장하고 나머지는 result에 저장
#            반복하다 n<k되면 남는건 빼기만 해야하는 값이니 n-1해준것을 result에 더해준다.

n,k = map(int,input().split())
result = 0
while True:
    target = (n//k)*k # k의 배수로 만들기
    result = n-target # 나머지는 빼기만 할거니까 그값 그대로 result에 넣기
    n = target 
    if n < k:
        break
    result += 1
    n //= k # n은 k를 나눈 몫이 된다.

result += (n-1) # 남은값은 1이 될때까지 빼기만 하면 되니까 result에 더해준다.
print(result)




