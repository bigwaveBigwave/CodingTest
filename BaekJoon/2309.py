#구하는 것 : 키의 합이 100인 일곱난쟁이의 키를 오름차순 출력
#구조화
# 아홉개의 키 입력받기
# 조합 적용
# 해당하는 조합을 오름차순 출력
import sys
from itertools import combinations
input = sys.stdin.readline
heights = [int(input().strip()) for _ in range(9)]

for cand in combinations(heights, 7):
    if sum(cand) == 100:
        for h in sorted(cand):
            print(h)
        break
