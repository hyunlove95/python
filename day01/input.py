# print : 글 나오도록 하는 기능
# input : 글을 입력하는 기능

# drama = input("Enter your input")
# print(f"입력 한 것 : {{{drama}}} 이 다")
#
# name = input("Enter your name")
# print(f"입력한 이름은 {{{name}}}가 맞다")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# color = input("Enter your color: ")
#
# print("{}   {}  {}".format(name, age, color))
# print(f"{color} {age} {name}")

date = input("Enter a date: ")
plan = input("Enter a plan: ")

print(f"{date}은 {plan}을 할 예정")
print("{}에 {}을 할 예정".format(plan, date))