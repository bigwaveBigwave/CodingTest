#구하는 것 :주어진 상수를 기준으로 정답인 x, y를 출력하기
#구조화
# 입력받기
# 연립방정식에 맞는 x, y를 반복문을 통해서 구하고 print하기

import sys
input = sys.stdin.readline
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            print(x, y)
            sys.exit()
