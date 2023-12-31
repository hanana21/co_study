# 문제: 식량 창고 N개가 일직선으로 있을 떄 최대한 많은 식량을 얻는 방법
#       단, 서로 인접한 창고를 공격하면 안된다.
# 해결 방법: 3개의 창고롤 생각해보면 1+3번창고 or 2번 창고 중 더 많은 식량을 고르는 것을 선택하면 된다.
#            (n-2)의 최대값+n or (n-1)의 최대값 비교
#            3번 창고부터 N창고까지 두상황 중 많은 식량을 가지는 경우를 dp테이블에 저장하는 것을 반복한다.  
n = int(input())
storage = list(map(int,input().split()))
d = [0]*101
d[1] = storage[0]
d[2] = max(d[1],storage[1])
for i in range(3,n+1):
    d[i] = max(d[i-2]+storage[i-1],d[i-1])
print(d[n])

