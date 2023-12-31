# 문제: 손님이 요청한 떡의 길이가 M일때 절단기의 최대 높이를 구하쇼
#       N = 떡의 갯수, M = 손님이 요청한 떡길이
# 푸는 방법: 파라트릭서치 문제 => 이진탐색(반복문을 이용하는것이 간결)
#            순차 탐색으로 하기에는 절단기의 범위가 많기 때문에 이진탐색으로 해야함
# 파라트릭 서치: 최적화문제(최소값,최고값 찾는)를 결정 문제(특정 범위안에 있는 값찾기)로 바꾸는 것

n,m = map(int,input().split())
rice_cakes = list(map(int,input().split())) 

start = 0
end = max(rice_cakes)

result = 0
while start <= end:
    total = 0
    mid = (start+end)//2
    for i in rice_cakes:
        if i > mid:
            total += i-mid
    if total < m:
        end = mid-1  
    else:
        result = mid 
        start = mid+1
        
print(result)


    