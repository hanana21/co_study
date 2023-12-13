# 3-3 책 풀이로 풀기 
# 풀이: 입력받은 데이터 중 가장 작은 데이터 찾기(min함수), 기존에 저장된 result와 비교하여 큰 값 저장
n,m = map(int,input().split())
result = 0
for i in range(n): # 한줄씩 입력 받기 
    data = list(map(int,input().split()))
    min_data = min(data)
    result = max(result,min_data)# 비교한 값중 큰값을 저장

print(max(result))