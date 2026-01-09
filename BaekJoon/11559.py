import sys
from collections import deque

input = sys.stdin.readline()

dx = {-1, 0, 1, 0}
dy = {0, 1, 0, -1}

board = [list(input().strip()) for _ in range(12)]

chain = 0

while True:
    visited = [[False] * 6 for _ in range(12)]
    popped = False

    #터질그룹 찾기
    for i in range(12):
        for j in range(6):
            if board[i][j] == '.' or visited[i][j]:
                continue
            color = board[i][j]
            q = deque([(i, j)])
            visited[i][j] = True
            cells = [(i,j)]

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
                        continue
                    if  visited[nx][ny]:
                        continue
                    if board[nx][ny] != color:
                        continue

                    visited[nx][ny] = True
                    q.append((nx, ny))
                    cells.append((nx, ny))

            if len(cells) >= 4:
                popped = True
                for x, y in cells:
                    board[x][y] = '.'

    if not popped:
        break

    chain += 1

    for c in range(6):
        write = 11
        for r in range(11, -1, -1):
            if board[r][c] != '.':
                board[write][c] = board[r][c]
                if write != r:
                    board[r][c] = '.'
                write -= 1

        for r in range(write, -1, -1):
            board[r][c] = '.'


print(chain)