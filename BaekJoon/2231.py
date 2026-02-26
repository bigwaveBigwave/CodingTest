#구하는 것 : 주어진 수가 만들어진 본래의 수를 구하기
#구조화
#입력받기
#m + m의 각 자릿수의 합을 만족하는 가장작은 M 출력

import sys
input = sys.stdin.readline


n = int(input().split())
start = max(1, n - 9 * len(str(n)))

ans = 0
for m in range(start, n):
    s = m + sum(map(int, str(m)))
    if s == n:
        ans = m
        break
print(ans)