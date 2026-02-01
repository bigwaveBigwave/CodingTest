#출력 : N/2 중 두 팀의 최소 차이값을 구하기
#구조화
# 1. 입력
# 2. 조합구하기 그 조합 마다 최솟값 갱신해서 출력

import sys
input = sys.stdin.readline
N = int(input())
board = []

for i in range(N):
    board[i].append(list(map(int, input().split())))

min = 0
for i in range(N):
    for j in range(N):
        difference = board[i][j] + board[j][i]

min = min(min, difference)
print(min)