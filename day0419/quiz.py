#  # 1번
#
# num1 = int(input("Please enter your num1 : "))
# num2 = int(input("Please enter your num2 : "))
# num3 = int(input("Please enter your num3 : "))
#
# avg = (num1 + num2 + num3) / 3
#
# print("The average is", round(avg, 2))
#
#
# # 2번
#
# num4 = int(input("Please enter your num4 : "))
# num5 = int(input("Please enter your num5 : "))
# num6 = int(input("Please enter your num6 : "))
#
# MaxNum4 = num4 >= num5 and num4 >= num6
# MaxNum5 = num5 >= num6 and num5 >= num4
# MaxNum6 = num6 >= num5 and num6 >= num4
#
# if MaxNum4:
#     print("가장 큰 정수 :", num4)
# elif MaxNum5:
#     print("가장 큰 정수 :", num5)
# elif MaxNum6:
#     print("가장 큰 정수 :", num6)


# 3번

num7 = int(input("Please enter your num7 : "))

for i in range(1, 101):
    if num7*i <= 100:
        print(num7*i)

