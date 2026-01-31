#구하는 것 : nxn 크기의 종이를 같은 수로 이루어진 종이로 나누어질 때까지 잘라서
# 같은수로이루어진 종이의 개수를 출력하기

#구조화
#입력받기
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = [0, 0, 0]

def solve(x, y, size):
    base = board[x][y]
    same = True

    for i in range(x, x + size):
        row = board[i]
        for j in range(y, y + size):
            if row[j] != base:
                same = False
                break
        if not same:
            break
    if same:
        cnt[base + 1] += 1
        return

    step = size // 3
    for dx in range(3):
        for dy in range(3):
            solve(x + dx * step, y + dy * step, step)
solve(0, 0, N)

print(cnt[0])
print(cnt[1])
print(cnt[2])

