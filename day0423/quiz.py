# 1번

# print("1.americano 2.lemonade 3.cafeLatte")
#
# menu = int(input("Please enter your menu : "))
# money = int(input("Please enter your money : "))
# americano = 3000
# lemonade = 4000
# cafeLatte = 3500
#
# if menu == 1 and money >= americano:
#     print(f"your menu is : \"americano\". 잔돈은 {money - americano}")
# elif menu == 2 and money >= lemonade:
#     print(f"your menu is : \"lemonade\". 잔돈은 {money - lemonade}")
# elif menu == 3 and money >= cafeLatte:
#     print(f"your menu is : \"cafeLatte\". 잔돈은 {money - cafeLatte}")
# else:
#     print("메뉴에 없거나 금액이 모자랍니다.")


# 2번

age = int(input("Please enter your age : "))
sinaebus = 1200
gangyakbus = 2000
maoulbus = 1000

print("1.시내버스 2.광역버스 3.마을버스")

while 1:
    bus = int(input("Please enter your bus : "))
    if bus == 1:
        bus = sinaebus
        break
    elif bus == 2:
        bus = gangyakbus
        break
    elif bus == 3:
        bus = maoulbus
        break
    else:
        print("그런 버스는 없다.")

if age <= 7 or age >= 65:
    discount = bus
elif 8 <= age <= 19:
    discount = bus*0.3
else:
    discount = 0
money = bus - discount

print(f"bus : {bus}, age : {age}, discount : {discount}, money : {money}")


# 3번

number = int(input("Please enter your number : "))

for i in range(1, 11):
    if (number * i) % 2 == 0:
        print(number*i)
