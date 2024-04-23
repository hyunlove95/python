fruits = ["apple", "banana", "cherry"]
# cherry == fruits[2]
print(fruits[1].upper())

numbers = [1,2,3,4]
mix = ["안녕", 1, "다시마", 3, True]
starbucks = [["아메리카노", "라떼"], ["주스", "에이드"], ["빵", "케이크"]]
print(starbucks[0])
print(starbucks[2][0])

# append[추가]
fruits.append("orange")
print(fruits)

# extend[확장]
fruits.extend(["strawberry", "grape"])
print(fruits)

# sort[정렬]
fruits.sort()
print(fruits)

# reverse[역정렬]
fruits.reverse()
print(fruits)

# pop[맨 뒤에 있는 거 빼기]
fruits.pop()
print(fruits)

# remove[제거]
fruits.remove("orange")
print(fruits)

# count
fruits.append("strawberry")
count = fruits.count("strawberry")
print(count)

# for 리스트는 요소를 하나씩 빼준다
for fruit in fruits:
    print(fruit)

