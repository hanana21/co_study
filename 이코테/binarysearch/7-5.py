# 문제: 손님이 요청한 부품갯수M,종류가 동빈이가 가지고 있는 부품일때 yes 아니면 no
# 풀이방법: 탐색 이용(이진탐색) 

n = int(input())
parts = list(map(int,input().split()))
parts.sort()

m = int(input())
requested_parts = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in requested_parts:
    result = binary_search(parts,i,0,n-1)
    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')
    
