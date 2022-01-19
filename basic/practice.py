print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4,99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

from random import *
print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)
print(int(random() * 10))

print(randrange(1,46))
print(randint(1,45))

sentence = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence)

jumin = "990120-1234567"

print("성별 : " + jumin[7])
print("연 : " +  jumin[0:2]) # 0 부터 2 직전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에서 부터): " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java"))
# print(python.index("Java"))

print(python.count("n"))