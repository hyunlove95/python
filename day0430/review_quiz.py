# 1번

# number = int(input("Enter a number: "))
# result = 0
#
# if number % 2 == 1:
#     for i in range(number+1):
#         if i % 2 == 1:
#             result += i
# else:
#     for i in range(number+1):
#         if i % 2 == 0:
#             result += i**2
#
# print(result)


# 2번

arr = [1,2,3,4,5,6,7,8,9]
k = int(input("Enter k: "))

if k % 2 == 1:
    for i in range(len(arr)):
        arr[i] *= k
else:
    for i in range(len(arr)):
        arr[i] += k

print(arr)
