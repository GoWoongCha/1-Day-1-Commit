# 함수를 사용하는 이유

# 함수를 사용하지 않은 경우
print("안녕하세요, 고객1님")
print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")

print("안녕하세요, 고객2님")
print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")

print("안녕하세요, 고객3님")
print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")

print("안녕하세요, 고객4님")
print("현재 프리미엄 서비스 사용기간이 5일 남았습니다.")

# 함수를 사용한 경우
def printMessage(name, data):
    print("안녕하세요, ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")

printMessage("고객1", 30)
printMessage("고객2", 15)
printMessage("고객3", 7)
printMessage("고객4", 5)