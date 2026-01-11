#문자열에서 가장 많이 출현한 알파벳 출력(여러개면 ?출력)

#입력받기
#알파벳마다 배열 선언(초기값 0) -> 65qnxj 122인데, 91부터 96은 무조건 0

#문자열의 각 순서대로 알파벳의 10진수로 만들어서 배열값을 1씩 증가
# 배열에서 가장 큰 값을 가진 인덱스가 여러개면 ?출력, 한개면 그 인덱스를 10진수 화

a = input().strip().upper()
b = [0]*26
for ch in a:
    b[ord(ch) - ord('A')] += 1

mx = max(b)
cnt = b.count(mx)


if cnt > 1:
    print("?")

else :
    print(chr(b.index(mx) + ord('A')))

