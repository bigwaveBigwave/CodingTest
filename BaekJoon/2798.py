#구하는 것 : 주어진 카드의 조합의 합을 출력
#구조화
# 입력받은 ㄱ카드 번호들을 조합으로 세개 뽑아서 m을 안 넘으면, 최대값 갱신해서 출력
import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())
nn = list(map(int, input().split()))
max_v = 0
for comb in combinations(nn, 3):
    if sum(comb) < m:
        max_v = max(max_v, sum(comb))
print(max_v)

