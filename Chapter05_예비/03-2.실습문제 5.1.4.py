korean = int(input("국어 >>> "))
math = int(input("수학 >>> "))
english = int(input("영어 >>> "))

everage = (korean + math + english) / 3

if 0 <= korean <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
    if everage >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")