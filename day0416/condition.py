# 제어문
# 실행 순서를 조작하는 문법
# 조건문(if, else, elif)
# num = int(input("Hello Python : "))
# if num > 0:
#     print("Hello World")

# num = int(input("Please enter a number : "))
# if num == 100:
#     print("You entered 100")
#
# elif 20 < num < 30:
#     print("You entered 20~30")

# num = int(input("Please enter a number : "))
# if num % 2 == 0:
#     print(num, "is an even number")
# else:
#     print(num, "is an odd number")

# password = input("Enter your password : ")
# if "!" in password and "IT" in password:
#     print("비밀번호 입력 완료!")
# else:
#     print("비밀번호 입력 실패!")
#
# num = int(input("Please enter a number : "))
# if num % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")

password = input("Enter your password : ")

if('!' in password and ('a' in password[0] or 'A' in password[0])):
    print("비밀번호 입력 완료")
else:
    print("비밀번호 입력 실패")


