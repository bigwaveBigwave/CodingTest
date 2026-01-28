#n번째 피보나치 수 구하기
#구조화
#n 입력받기
#초기값 설정: 0일 때 0 , 1일 때 1, 그 이상이면 함수(n-1) + 함수 (n-2)
import sys
input = sys.stdin.readline

def fibo(n) :
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input())
print(fibo(n))