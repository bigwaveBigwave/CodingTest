import sys

count = sys.stdin.readline().rstrip()

for i in range(int(count)):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result = a+b
    print(result)