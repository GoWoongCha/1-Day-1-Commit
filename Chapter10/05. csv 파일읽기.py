import csv

file = open("C:/Users/User/Desktop/1Day_1Commit/Chapter10/student.csv", "r", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()