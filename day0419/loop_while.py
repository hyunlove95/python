# loop_while

# x = 10
# while x > 0:
#     print(x)
#     x -= 1

# x = 10
# while x != 0:
#     x = int(input("0 넣으면 멈춤 : "))
#
# while True:
#     x = int(input("0 넣으면 멈춤 : "))
#     if x == 0:
#         break

# print('1 : 아아, 2 : 아이스 라떼, 0은 주문 끝')
#
# while 1:
#     x = int(input('주문 : '))
#     if x == 0:
#         break
#     elif x == 1:
#         print("아아\n")
#     elif x == 2:
#         print("아이스 라떼\n")

# print("1.Python 2.Java 3.c++ 4.프로그램 종료")
# while 1:
#     x = int(input('\nEnter a number: '))
#     if x == 1:
#         print("Python")
#     elif x == 2:
#         print("Java")
#     elif x == 3:
#         print("c++")
#     elif x == 4:
#         print("프로그램 종료")
#         break
#     else:
#         print("Invalid input")

print('1.더하기 2.빼기 3.곱하기 4.제곱 5.나누기(몫)')
while 1:
    x = int((input("\n기호 : ")))
    if x == 0:
        print("프로그램 종료")
        break

    num1 = int(input('Enter a num1 : '))
    num2 = int(input('Enter a num2 : '))

    if x == 1:
        print(f'{num1}+{num2}={num1+num2}')
    elif x == 2:
        print(f'{num1}-{num2}={num1-num2}')
    elif x == 3:
        print(f'{num1}*{num2}={num1*num2}')
    elif x == 4:
        print(f'{num1}의{num2}제곱은 {num1**num2}')
    elif x == 5:
        print(f'{num1}/{num2}={num1//num2}   ...     {num1%num2}')
    else:
        print("Invalid input")

