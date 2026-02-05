#구하는 것 : N개의 힌트를 보고 영수의 숫자의 경우의 수를 출력
#구조화
# N번 반복
#  각 줄 마다 스트라이크와 볼을 분석
#   스트라이크 : 각 자릿수 고정을 경우의 수로 생각
#   볼 : 각 숫자를 경우의 수로 생각
# 경우의 수 출력
import sys
from collections import permutations
input = sys.stdin.readline
N = int(input())
for i in range(N):
    num, st, boll = map(int, input())
