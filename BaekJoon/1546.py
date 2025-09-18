count = int(input())
numbers = [int(input()) for _ in range(count)]

max_value = numbers[0]

for i in numbers:
    if max_value < i:
        max_value = i;


for k in numbers:
    total = k / max_value * 100


print((total-100)/count)