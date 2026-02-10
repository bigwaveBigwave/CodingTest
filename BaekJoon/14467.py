# 소가 길을 건넌 횟수를 출력하기
#구조화
# 소의 이전 방향을 기억 -> 저장 공간 필요 -> 배열
# 방향이 달라지면 +1

import sys
input = sys.stdin.readline

N = int(input())
last = [-1] * 11
ans = 0

for _ in range(N):
    cow, pos = map(int, input().split())

    if last[cow] == -1: #첫 등장
        last[cow] = pos
    else :
        if last[cow] != pos:# 위치변경 -> 길 건넘 1회
            ans += 1
            last[cow] = pos# 마지막 위치 갱신

print(ans)