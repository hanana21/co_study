# 문제: M번 더한 총합이 최대가 되게 하기, 단 같은 인덱스를 K번 연속으로 더할 수 없다. 
# 풀이 방법: 가장 큰수와 그다음 큰수만 이용하는 문제이다. 
#           큰 순서대로 배열하고 0번과 1번이 같다면 0번 값을 m번 더하고 
#           아니라면 0번 값을 더하다가 count = k 일때 1번 값을 한번 더해주고 count=0 시켜줘서 다시 0번 값을 더하게 한다.
# => 시간 복잡도가 상당해보인다. 

n,m,k = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr,reverse=True)
sum = 0
count = 0

for i in range(m):
    if arr[0]==arr[1]:
        sum += arr[0] 
    else:
        if count == k:
            sum += arr[1]
            count = 0
        else: 
            sum += arr[0]
            count +=1
            
print(sum)