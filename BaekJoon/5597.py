a = [0] * 31

for _ in range(28):
    b = int(input())
    a[b] = 1

for i in range(1, 31):
    if a[i] == 0:
        print(i)