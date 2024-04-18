# for 반복문

# for 변수 in range(횟수):
# 0 ~ n-1까지
# for i in range(10):
#     print(i)

# num = int(input("Enter a number: "))
#
# for i in range(num):
#     print(i)

gugudan = int(input("Enter gugudan : "))

for i in range(10):
    if i > 0:
        print(f"{gugudan}*{i}={gugudan*i}")
