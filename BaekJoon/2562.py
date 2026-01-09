b = [0,0,0,0,0,0,0,0,0]

max_val = 0
max_i = 0
for i in range(len(b)):
    a = int(input())
    b[i] = a
    if max_val < b[i]:
        max_val = b[i]
        max_i = i


print(max_val)
print(max_i + 1)