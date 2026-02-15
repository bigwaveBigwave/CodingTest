#구하는 것 : 전구상태출력
# 구조화
#  전구 개수, 명령어 개수 입력받기
#  현재 전구 상태 배열 입력받기
#  명령어 마다 명령어 수행하기
#  전구상태 출력

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
flash = list(map(int, input().split()))
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        flash[b-1] = c
    elif a == 2:
        for i in range(b-1, c):
            if flash[i] == 0:
                flash[i] = 1
            elif flash[i] == 1:
                flash[i] = 0
    elif a == 3:
        for i in range(b-1, c):
            flash[i] = 0
    elif a == 4:
        for i in range(b-1, c):
            flash[i] = 1

print(*flash)

