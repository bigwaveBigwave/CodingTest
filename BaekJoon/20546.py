#구하는것 : 준현/성민의 자산 중 더 큰 것을 출력 같으면 same
#구조화
# 현금 입력받기
# 주식 남은 값 배열 초기화
# 주가 배열 입력받기
import sys
input = sys.stdin.readline
money = int(input())
p = list(map(int, input().split()))

#준현
b_cash = money
b_stock = 0
for price in p:
     if b_cash >= price:
         cnt = b_cash // price
         b_stock += cnt
         b_cash -= cnt*price
b_asset = b_cash + b_stock * p[-1]

#성민
t_cash = money
t_stock = 0

for i in range(3, 14):
    if p[i-3] < p[i-2] and p[i-2] < p[i-1] and p[i-1] < p[i]:
        if t_stock > 0:
            t_cash += t_stock*p[i]
            t_stock = 0

    elif p[i-3] > p[i-2] and p[i-2] > p[i-1] and p[i-1] > p[i]:
        if t_cash >= p[i]:
            cnt = t_cash // p[i]
            t_stock += cnt
            t_cash -= cnt*p[i]
t_asset = t_cash + t_stock*p[-1]

if b_asset > t_asset:
    print("BNP")
elif b_asset < t_asset:
    print("TIMING")
else:
    print("SAMESAME")
