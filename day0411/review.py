# 콘솔창에 내용 출력 기능
print("파이썬 공부 복습")

# 변수
# 1. 숫자 시작 안됨
# 2. 특수문자 _ 빼고 안됨
# 3. 예약어 안됨
# 4. 두 단어 이상 합쳐지면 스네이크, 카멜 중 골라서 짓기

# 콘솔창에 유저에게 글을 입력받는 기능
# number = input("Enter your number: ")
# print(f"Your number is {number}")

date = input("Enter your date: ")
incident = input("Enter your incident: ")

print(f"Your date is {date}, your incident is {incident}")


breakfirst = input("Enter your breakfirst: ")
lunch = input("Enter your lunch: ")
dinner = input("Enter your dinner: ")

print("{}, Your 식사 is {}, {}, {}".format(date, breakfirst, lunch ,dinner))

