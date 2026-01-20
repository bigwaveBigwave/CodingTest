#알파벳배열을 출력하는데, 주어진 문자에 알파벳이 없으면 -1, 있으면 위치를 출력
#문자열입력받기
#문자열 길이마다 문자 확인 -> 문자의 인덱스를 배열에 삽입
import sys
input =sys.stdin.readline
pos = [-1] * 26
s = input().strip()
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    if pos[idx] == -1:
        pos[idx] = i
    #아스키코드 : 문자를 숫자로 바꾸는 것. a = 96


print(*pos)