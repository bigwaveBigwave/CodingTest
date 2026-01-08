total = int(input())
kind = int(input())
total_part = 0
for _ in range(kind) :
    price, count = map(int, input().split())
    total_part += price * count

if total_part == total :
    print("Yes")

else :
    print("No")