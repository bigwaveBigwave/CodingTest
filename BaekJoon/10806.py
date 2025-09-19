
n = int(input())
numbers = list(map(int, input().split()))
findNumber = int(input())

count = numbers.count(findNumber)
print(count)