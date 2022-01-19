for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1,6):
    print("대기번호 : {0}".format(waiting_no))

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")