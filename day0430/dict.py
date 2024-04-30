person = {
    'name': "John"
    , 'age': 25
    , 'city': "New York"
    , 'coffeeList': ["아메리카노", "카페라떼", "카푸치노"]
    , 'academy' : {
        'first': "java"
        , 'second': "python"
        , 'third': "javascript"
    }
}

print(f"이름 : {person['name']}, 동네 : {person['city']}, "
      f"3번째 커피 : {person['coffeeList'][2]}, "
      f"학원의 3번째 수업 : {person['academy']['third']}")
print(person['coffeeList'][1])
print(person['academy']['first'])

# 데이터 생성
person["gender"] = "male"

# 데이터 삭제
del person["city"]
print(person)

print(person.keys()) # key
print(person.values()) # value
print(person.items()) # key-value
print(person)
