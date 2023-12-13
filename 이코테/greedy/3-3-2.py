# 3-3문제 이중 for문으로 풀기 
# 풀이: 입력받은 data에서 가장 작은 값을 찾고 저장된 기존의 최고값과 비교하여 더 크면 저장(n번 반복)
n,m = map(int,input().split())
result = 0
for i in range(n): 
    data = list(map(int,input().split()))# 한줄씩 입력 받기
    min_data = 10001 #임의의 수 대충 큰거 아무거나적음 
    for d in range(data):
        min_data = min(min_data,d) # 가장 작은 값 찾기 위해 하나 하나 비교하기
    result = max(result,min_data) # 작은 값중 가장 큰값 찾기
print(result)     
    



    
