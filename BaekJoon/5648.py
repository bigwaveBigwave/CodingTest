# 구조화
#  배열 입력받기
#  각 숫자를 문자열로 바꾼뒤 뒤집기
#  다시 정수로 변환(0제거)
#  오름차순 정렬
#  한 줄에 하나씩 출력
import sys
data = sys.stdin.read().split()

n = int(data[0])
numbers = data[1:]

result = []

for num in numbers:
    reversed_num = int(num[::-1])
    result.append(reversed_num)

result.sort()

for r in result:
    print(r)

