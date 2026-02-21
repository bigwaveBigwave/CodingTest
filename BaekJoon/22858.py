import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))

d = [x - 1 for x in d]
cur = s
for _ in range(k):
    prev = [0] * n
    for i in range(n):

        prev[d[i]] = cur[i]
    cur = prev

print(*cur)