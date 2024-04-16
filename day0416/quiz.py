import math

# 1번
won = int(input("Please enter korea won : "))

print(f"{won//1398}달러 {round((won/1398-won//1398)*100)}센트") # 소수점만 남기고 100을 곱해 2자리까지만

# 2번
num1 = int(input("Please enter first number : "))
num2 = int(input("Please enter second number : "))

print(f"합 : {num1+num2}, 차 : {num1-num2}, 곱 : {num1*num2}, "
      f"몫 : {num1//num2}, 나머지 : {num1%num2}, 첫 번째 수의 두번째 수의 제곱 : {num1**num2}")


# 3번
radius = int(input("Please enter radius : "))

print("원의 둘레 : {}, 원의 넓이 : {}"
      .format(round(2*math.pi*radius, 2), round(math.pi*radius**2, 2)))