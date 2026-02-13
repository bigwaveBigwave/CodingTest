#구하는 것 : 최대 피로도를 안 넘으면서 최대로 할 수 있는 일
#구조화
# 매 시간마다 선택지 두 개(일을 한다/안 한다)
# 일을 최대로 하려면 ? 24시간 내에 할 수 있으면 일을 하기(greedy)
import sys
input = sys.stdin.readline
a, b, c, m = map(int, input().split())

#예외처리
if a > m:
    print(0)
else:
    fatigue = 0
    work = 0

    for _ in range(24):
        if fatigue + a <= m:
            fatigue += a
            work += b
        else:
            fatigue -= c
            if fatigue < 0 :
                fatigue = 0
print(work)