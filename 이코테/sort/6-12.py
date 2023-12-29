# 문제: 두배열의 원소를 K번 바꿔치기 가능함, A의 모든 원소의 합이 최대가 되게 해준다.
# 해결 방법: A의 최소값과 B의 최대값을 바꾸기

n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
for i in range(k):
    if a[i] < b[i]: 
        a[i] = b[i]
    else: # 원소의 크기가 같거나 클때는 더이상 바꿀필요 없으니(이미 정렬된 상태) 걍 탈출
        break
print(sum(a))



