# 실습문제 4.3.2
# 사용자로부터 태어난 연도를 입력받으면
# 현재 나이를 출력하기

x = input("태어난 연도를 입력하세요 >>> ")
age = 2022 - int(x) + 1
print("현재 나이는 " + str(age) + "세 입니다.")

# 한 줄 안에 int와 str을 동시에 표시하는 방법으로는 두 가지가 있다.
# 1. print("The number is", x)
# 2. print("The number is" + str(x))

# 문제풀이 
year = int(input("태어난 연도를 입력하세요 >>> "))
age = 2021 - year + 1
print("현재 나이는 ", age, "세 입니다.")