#구해야할 것 : 색종이가 덮은 영역의 넓이
#구조화
#1. 테스트케이스입력받고 각 케이스마다 붙이는 x, y 입력받기
#2. 300에서 겹치는 부분 빼기
#3. 겹치는 부분 :
#100바이100 행렬에서 xn, yn을 입력받으면 거기서 +100, +100만큼을 +1하기
#마지막에 전체 ㅎ ㅐㅇ렬에서 2이상인 부분의 개수를 더해서 300에서 빼기

import sys
input = sys.stdin.readline
board = [[0]*100 for _ in range(100)]
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

ans = 0
for i in range(100):
    ans += sum(board[i])
print(ans)
