#출력 : N/2 중 두 팀의 최소 차이값을 구하기
#구조화
# 1. 입력
# 2. 조합구하기 그 조합 마다 최솟값 갱신해서 출력

import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
players = list(range(N))

for start in combinations(players[1:], N // 2 - 1):
    start = (0,) + start
    link = [p for p in players if p not in start]

    start_score = 0
    link_score = 0
    for i, j in combinations(start, 2):
        start_score += board[i][j] + board[j][i]
    for i, j in combinations(link, 2):
        link_score += board[i][j] + board[j][i]

    ans = min(ans, abs(start_score - link_score))
print(ans)


