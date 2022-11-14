import random

def get_random_number():
    number = random.randint(1, 45)
    return number

lotto_number = []
count = 0

while True:
    if (count > 5):
        break
    random_number = get_random_number()
    if random_number not in lotto_number:
        lotto_number.append(random_number)
        count += 1

lotto_number.sort()
for num in lotto_number:
    print(num, end = " ")
