#구하는 것 : 로봇청소기가 작동을 멈출때까지 청소한 칸의 개수 출력
#구조화
#입력, 방문배열, 전체배열
#bfs
import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
visit=[[0] * M for _ in range(N)]
board=[[0] * M for _ in range(N)]
cx, cy, d = map(int, input().split())
for i in range(N):
        board[i].append(map(int, input().split()))

visit[cx-1][cy-1] = 1
q = deque()
q.append((cx-1, cy-1))
while q:
    cur_x, cur_y = q.popleft()
    q.pop()
    for dir in range(4):
        nx = cur_x + dx[dir]
        ny = cur_y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visit[nx][ny] != 0 or board[nx][ny] == 1:
            continue
        visit[nx][ny] = visit[cur_x][cur_y] + 1
        q.append((nx, ny))