import sys
sys.setrecursionlimit(10**6)

def func(a, b, n):
    if n == 1:
        print(a, b)
        return
    c = 6 -a - b
    func(a, c, n - 1)
    print(a, b)
    func(c, b, n - 1)


k = int(sys.stdin.readline())
print(2 ** k - 1)
func(1, 3, k)