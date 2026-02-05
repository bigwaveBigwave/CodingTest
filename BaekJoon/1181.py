#구하는 것 : N개의 단어들을 짧은 순, 사전순으로 정렬해서 출력하기
#구조화
# N크기의 배열 선언, 반복 입력
# 정렬
#   1. 문자열 길이 기준
#   2. 사전순 기준
# 정렬된 단어 출력
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().strip())
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
#arr.sort()
print(*arr)