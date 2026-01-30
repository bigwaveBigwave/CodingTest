import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

board = [[0]*(N+1) for _ in range(N+1)]
#0:빈칸, 1:뱀, 2: 사과
for _ in range(K):
    a, b = map(int, input().split())
    board[a][b] = 2

l = int(input().strip())
turns = deque()
for _ in range(l):
    c, d = input().split()
    turns.append((int(c), d))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

snake = deque()
snake.appendleft((1, 1))
dir = 1
second = 0

while True:
    dir %= 4

    x,y = snake[0]
    board[x][y] = 1
    second += 1

    nx = x + dx[dir]
    ny = y + dy[dir]

    if nx < 1 or nx > N or ny < 1 or ny > N:
        break
    if board[nx][ny] == 1:
        break

    if board[nx][ny] != 2:
        tx, ty = snake.pop()
        board[tx][ty] = 0
    else:
        board[nx][ny] = 0

    if turns and turns[0][0] == second:
        _, ch = turns.popleft()
        if ch == 'L':
            dir += 1
        else:
            dir += 3

    snake.appendleft((nx, ny))

print(second)
