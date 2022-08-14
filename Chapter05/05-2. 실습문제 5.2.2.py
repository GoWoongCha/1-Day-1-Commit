# 실습문제 5.2.2
# 턱걸이 평균 측정 프로그램을 만들어보자. 먼저, 턱걸이 횟수를 저장할 빈 리스트를 만든다.
# 그리고 일주일 간의 턱걸이 횟수를 입력받아 리스트에 저장한다. 리스트에 저장된 데이터의
# 평균을 구해 출력한다.

empty = []

empty.append(int(input("1일차 턱걸이 횟수 >>> ")))
empty.append(int(input("2일차 턱걸이 횟수 >>> ")))
empty.append(int(input("3일차 턱걸이 횟수 >>> ")))
empty.append(int(input("4일차 턱걸이 횟수 >>> ")))
empty.append(int(input("5일차 턱걸이 횟수 >>> ")))
empty.append(int(input("6일차 턱걸이 횟수 >>> ")))
empty.append(int(input("7일차 턱걸이 횟수 >>> ")))

avg_value = sum(empty) / len(empty)

print(avg_value)

# 문제풀이

data = [] # 빈 리스트 생성

x = int(input("1일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("2일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("3일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("4일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("5일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("6일차 턱걸이 횟수 >>> "))
data.append(x)
x = int(input("7일차 턱걸이 횟수 >>> "))
data.append(x)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total / 7

print(int(avg))