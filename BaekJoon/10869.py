numbers = list(map(int, input().split()))

def plus(a, b):
    return a+b;

def minus(a, b):
    return a-b;

def multifly(a, b):
    return a*b;

def devide(a, b):
    return int(a/b);

def devide2(a, b):
    return a%b;

print(plus(numbers[0], numbers[1]))
print(minus(numbers[0], numbers[1]))
print(multifly(numbers[0], numbers[1]))
print(devide(numbers[0], numbers[1]))
print(devide2(numbers[0], numbers[1]))