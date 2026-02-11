#구하는것 : 준현/성민의 자산 중 더 큰 것을 출력 같으면 same
#구조화
# 현금 입력받기
# 주식 남은 값 배열 초기화
# 주가 배열 입력받기
import sys
input = sys.stdin.readline
n = int(input())
juga = []
s = []
j = []
ss = n
jj = n
for _ in range(14):
    juga.append(int(input))

for i in juga:
    if ss>i:
        t = 0
        while(ss>=i*t):
            t+=1
        ss = ss - i*t
        s[i] = i*t+juga[i]

for i in juga:
    if jj > i:
        t = 0
        while (ss >= i * t):
            t += 1
        s[i] = n - i * t + juga[i]

