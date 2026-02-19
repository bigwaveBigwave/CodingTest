#구하는 것 : 연료 합의 최솟값
#구조화
# 행렬 입력받기
# 방향 배열 선언
# 갈 수 있는 세 방향 중 가장 작은 값이 있는 방향 구하기(이전으 ㅣ방향과 같다면 그 다음 최솟값)
# 계속 연료값을 합산하기
import sys
from collections import deque
input = sys.stdin.readline
n ,m = map(int, input().split)
ans = 0#연료값
board = [][]
for i in range(n):
    board[i].append(list(map(int, input().split())))

dx = [1, 1, 1]
dy = [-1, 0, 1]

a = deque()
#첫째줄에서 최솟값 구하기
min = 100
for i in range(m):
    if min > board[0][i]:
        min = board[0][i]
        a.push({0, i})
while a.empty():
    x, y = a.


