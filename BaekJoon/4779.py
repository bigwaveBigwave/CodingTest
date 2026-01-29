#구하는 것 : 모든 선의 길이가 1일때 선을 출력하기
#구조화
#EOF 입력받기
#각 입력마다 -을 3^N개 배열에 집어넣기
#나누기 3

import sys
def cantor(n : int) -> str:
    if n == 0:
        return "-"
    prev = cantor(n - 1)
    gap = " " * (3 ** (n-1))
    return prev + gap + prev

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    n = int(line)
    sys.stdout.write(cantor(n) + "\n")