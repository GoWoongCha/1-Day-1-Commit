# 실습문제 5.1.4

# 프로그램 사용자로부터 국어, 수학, 영어 성적이 입력된다. 세 과목의 평균점수가 80점 이상이면 합격이다.
# 그런데 점수에 따라 합격 또는 불합격이 정해지는 프로그램에 오류가 발생했다. 80점 이상일 경우 불합격이
# 표시되도록 프로그램을 작성해보자. (단, 0점에서 100점 사이의 숫자를 입력하지 않으면 "잘못
# 입력하였습니다." 를 출력하자)

korean = int(input("국어 >>> "))
math = int(input("수학 >>> "))
english = int(input("영어 >>> "))

everage = (korean + math + english) / 3

if korean < 0 or korean > 100:
    print("잘못 입력했습니다.")
elif  math < 0 or math > 100:
    print("잘못 입력했습니다.")
elif english < 0 or english > 100:
    print("잘못 입력했습니다.")
elif everage < 80:
    print("합격")
elif everage >= 80:
    print("불합격") # 직접 실습한 결과

# 문제풀이

ex_korean = int(input("국어 >>> "))
ex_math = int(input("수학 >>> "))
ex_english = int(input("영어 >>> "))

total = ex_korean + ex_math + ex_english
avg = total / 3

# 방법 1
if 0 <= ex_korean <= 100 and 0 <= ex_math <= 100 and 0 <= ex_english <= 100:
    if avg >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.") # 중첩 조건문 활용

# 방법 2
if ex_korean < 0 or ex_korean > 100 or ex_math < 0 or ex_math > 100 or ex_english < 0 or ex_english > 100:
    print("잘못 입력하였습니다.")
elif avg >= 80:
    print("불합격")
else:
    print("합격")

# 2022년 08월 09일 1차 문제풀이 완료
# 향후 오답풀이 필요