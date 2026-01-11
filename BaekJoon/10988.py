#입력받은 문자열을 역순배치했을 때 순행과 일치하는지 출력하기
#문자열입력받기
#역순배치하기
#같은지 확인

literal = input()
reverse = literal[::-1]
answer = True
if reverse == literal:
    print(1)
else :
    print(0)