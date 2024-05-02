# map(how, target): target을 바꿔주기
numList = [i for i in range(10)]

result1 = list(map(lambda x: x+100, numList))

print(result1)

# filter : targer을 필터링해줌
result2 = list(filter(lambda x: x % 2 == 0, numList))
print(result2)


fruits = ["apple", "banana", "cherry", "kiwi"]

result3 = list(filter(lambda x: len(x) <= 5, fruits))
print(result3)

result4 = list(filter(lambda x: "a" in x, fruits))
print(result4)

emailList = ["abc@naver.com", "mega@gmail.com", "korea@daum.net"]
result5 = list(map(lambda x: x.split("@")[0], emailList))
print(result5)