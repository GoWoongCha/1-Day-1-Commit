# 실습문제 4.3.1
# 사용자로부터 두 개의 숫자를 입력받고
# 더한 결과를 출력하기

a = input("첫 번째 숫자를 입력하세요 >>> ")
b = input("두 번째 숫자를 입력하세요 >>> ")

print(a + b) # 직접 시도한 실습, (결과, 2040)

# 문제풀이

x = input("첫 번째 숫자를 입력하세요 >>> ")
y = input("두 번째 숫자를 입력하세요 >>> ")

# 자료형 확인하기 : type(x)
# str = string = 문자열

print(type(x))

# 숫자형으로 변환
# int 함수를 사용 : int(데이터)

result = int(x) + int(y)
print(result)