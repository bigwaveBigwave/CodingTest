#구해야할 것 : 0이 가장 많아지도록 1이라는 벽을 세워서 2의 확산을 막은 뒤 1의 영역의 최댓값을 구하기
#구조화
#1. 지도 크기 입력 받기
#2. 지도 크기만큼 배열 선언
#2-1. 지도 크기 만큼 방문배열 선언
#3. 지도 입력받기
#4.0인 곳을 1로 바꿨을 때 2가 확산
import sys
from collections import deque

input = sys.stdin.readline

# 1. 입력
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

frees = []
virus = []

free_cells = 0


# 2. 빈칸, 바이러스 좌표 수집
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            frees.append((i, j))
            free_cells += 1
        elif board[i][j] == 2:
            virus.append((i, j))


# 2. 바이러스가 퍼지는 칸 수 계산 BFS
def bfs_spread_count():
    q = deque(virus)
    vis = [[False] * m for _ in range(n)]

    spread = 0 #바이러스가 차지한 칸 수 (기존 바이러스 포함)

    while q:
        x, y = q.popleft()
        spread += 1

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if board[nx][ny] != 0 or vis[nx][ny]:
                continue
            vis[nx][ny] = True
            q.append((nx, ny))

    return spread

#4. 3개 벽 세우기 브루트포스
ans = 0
V = len(virus)

for i in range(len(frees)):
    x1 ,y1 = frees[i]
    board[x1][y1] = 1

    for j in range(i + 1, len(frees)):
        x2, y2 = frees[j]
        board[x2][y2] = 1

        for k in range(j + 1, len(frees)):
            x3, y3 = frees[k]
            board[x3][y3] = 1

            #바이러스 확산 된 총 칸수(기존 바이러스 포함)
            spread_total = bfs_spread_count()

            #안전영역 계산:
            #원래 빈칸 free_cells 중 3개는 벽으로 변했음 -> free_cells - 3
            # 그 중 바이러스가 퍼져서 먹은 빈칸의 개수를 빼야 함
            #spread_total에는 기존 바이러스 칸 V가 포함돼있으니
            #새로 먹은 빈칸 = spread_total - V
            safe = (free_cells - 3) - ( spread_total - V)

            if safe > ans:
                ans = safe

            board[x3][y3] = 0
        board[x2][y2] = 0
    board[x1][y1] = 0
print(ans)