# 1번
# number = int(input("Enter a number : "))

# isPositive = number > 0
# isNegative = number < 0
# isOdd = number % 2 == 1
# isEven = number % 2 == 0

# if number > 0:                          # isPositive
#     if number % 2 == 0:                 # isEven
#         print(number, "is 양의 짝수")
#     else:                               # isOdd
#         print(number, "is 양의 홀수")
# elif number == 0:
#     print(number, "is 0")
# else:                                   # isNegative
#     if number % 2 == 0:                 # isEven
#         print(number, "is 음의 짝수")
#     else:                               # isOdd
#         print(number, "is 음의 홀수")

# positionX = int(input("Enter a positionX: "))
# positionY = int(input("Enter a positionY: "))
#
# isPositiveX = positionX > 0
# isPositiveY = positionY > 0
# isNegativeY = positionY < 0
# isZeroX = positionX == 0
# isZeroY = positionY == 0
#
# #                   나중에
# # -------------------------------------------------------
# if isPositiveY:
#     if isPositiveX:
#         print("1사분면")                   # x>0, y>0
#     elif isZeroX:
#         print("X축 위에 존재함")
#     else:
#         print("2사분면")                   # x<0, y>0
# elif isNegativeY:
#     if isPositiveX:
#         print("3사분면")                   # x>0, y<0
#     elif isZeroX:
#         print("X축 위에 존재함")
#     else:
#         print("4사분면")                   # x<0, y<0
# # -------------------------------------------------------


account = int(input("Enter your account : "))

if account >= 200000:
    discount = 0.2
elif account >= 100000:
    discount = 0.1
elif account >= 50000:
    discount = 0.05
else:
    discount = 0

print(f"구매액 : {account}, 할인율 : {discount*100}%, "
      f"할인 금액 : {account*discount}, 최종 결재 금액 : {account-account*discount}")










