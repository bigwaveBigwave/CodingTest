#구하는 것 : 주어진 좌표를 보고 직사각형을 만들 수 있는 좌표 출력
#구조화
# x,y 중 한번만 나온 좌표가 나머지 값.
# x,y값을 각각 입력받고 배열에 추가
# 배열에서 한번밖에 없는 수가 있으면 그 수를 출력

import sys
input = sys.stdin.readline

x = []
y = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in x:
    if x.count(i) == 1:
        rx = i

for i in y:
    if y.count(i) == 1:
        ry = i

print(rx, ry)

