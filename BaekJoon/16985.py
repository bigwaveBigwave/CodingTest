#주어진 3차원 미로를 탈출하는 최단 거리를 출력(탈출 못하면 -1 출력)
#구조화
#입력받기
# 2차원 배열 5개
#각 경우의 수마다 bfs 돌리기
#최단거리 갱신

import sys
input = sys.stdin.readline
from collections import deque
from itertools import permutations, product

# board[dir][i][j][k] : i번째 판을 시계방향으로 dir번 돌렸을 때 (j, k) 값
board = [[None] * 5 for _ in range(4)]
def rotate90(b):
    #5x5 시계방향 90도 회전
    return [list(row) for row in zip(*b[::-1])]

# 입력 + 4회전 미리 생성
for i in range(5):
    b0 = [list(map(int, input().split())) for _ in range(5)]
    b1 = rotate90(b0)
    b2 = rotate90(b1)
    b3 = rotate90(b2)
    board[0][i] = b0
    board[1][i] = b1
    board[2][i] = b2
    board[3][i] = b3

#3D BFS
dx = [1, 0, 0, 0, 0, -1]
dy = [0, 1, -1, 0, 0, 0]
dz = [0, 0, 0, 1, -1, 0]

INF = 10**9

def solve(maze):
    #시작/끝 막혀있으면 불가
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return INF

    dist = [[[0]*5 for _ in range(5)] for _ in range(5)]
    q = deque()
    q.append((0, 0, 0))
    dist[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        for d in range(6):
            nx, ny, nz = x+ dx[d], y + dy[d], z +dz[d]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 or nz < 0 or nz >= 5:
                continue
            if maze[nx][ny][nz] == 0 or dist[nx][ny][nz] != 0:
                continue
            if nx == 4 and ny == 4 and nz == 4:
                return dist[x][y][z]
            dist[nx][ny][nz] = dist[x][y][z] + 1
            q.append((nx, ny, nz))
    return INF

ans = INF

# 판 쌓는 순서 : 5팩토리얼
for order in permutations(range(5)):
    #tmp = 0..0123으로 4^5 회전 조합 만들기
    for tmp in range(1024):
        brute = tmp
        maze = [[[0] * 5 for _ in range(5)] for _ in range(5)]
        #maxe[x][y][z] 처럼 쓰기 위해 x층 기준준

        for z in range(5):
            rot = brute % 4
            brute //=4

            plate_id = order[z]
            layer = board[rot][plate_id]

            for x in range(5):
                for y in range(5):
                    maze[z][x][y] = layer[x][y]

        ans = min(ans, solve(maze))
        if ans == 12:
            print(12)
            sys.exit(0)

print(-1 if ans == INF else ans)



