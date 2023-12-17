# 팩토리얼 예제

# 재귀적
def factorial_recursive(n):
    if n<1 : # 종료조건
        return 1 
    return n * (factorial_iterative(n-1))

# 반복적
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result 

print(factorial_iterative(5))
print(factorial_recursive(5))
