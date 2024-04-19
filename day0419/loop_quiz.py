# 1번

# Sum = 0
#
# for i in range(1, 101):
#     Sum += i
#
# print(Sum)


# 2번

fruit = input("과일 입력 : ")
answer = ''
for i in fruit:
    if not i in "aiueo":
        answer += i

print(answer)
