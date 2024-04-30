# comprehension
# arr = []
# for i in range(101):
#     arr.append(i)
# print(arr)
#
# a = [i for i in range(101)]
# print(a)
#
# apple = [i for i in "apple"]
# print(apple)
#
# c = [i for i in range(11) if i % 2 == 0]
# print(c)
#
# d = [i for i in range(101) if i % 2 == 1]
# print(d)
#
# e = [i**2 for i in range(101) if i % 2 == 0]
# print(e)
#
# f = [i+10 for i in range(11) if i % 2 == 1]
# print(f)

fruits = ["apple", "orange", "pear", "kiwi", "grape"]
g = [len(i) for i in fruits if "i" in i]
print(g)

h = [i+10 if i % 2 == 1 else i+20 for i in range(101)]

fruit = [len(i) if len(i) <= 5 else i.upper() for i in fruits]
print(fruit)