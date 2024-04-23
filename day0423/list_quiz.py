# 1번
# numList = []
# for i in range(5):
#     num = int(input("Enter a number: "))
#     numList.append(num)
#
# for j in range(numList):
#     num = numList[0]*3
#     numList.remove(numList[0])
#     numList.append(num)
#     print(numList)


# 2번
numList2 = []
for i in range(5):
    num = int(input("Enter a number: "))
    numList2.append(num)

numList2.sort()
print(numList2)
numList2.reverse()
print(numList2)
print(numList2[0])
