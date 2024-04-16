# compare_logic
# >,<,>=,<=,==,!=
a = 10
b = 20
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

# 논리 연산자
# and, or, not
c = 5
d = 3
# and : 모든 조건이 참이면 참
print(c < d and c == 5 and d == 3)

# or : 하나라도 참이면 참
print(c < d or c == 7 or d == 3)

# not : 조건의 반대를 반환
print(not(c < d))

print (1)

result = c < d and c == 5
result1 = not(c >= d) or not(c != 5)

print(result)
print(result1)
