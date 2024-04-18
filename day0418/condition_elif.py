# condition_elif
# score = int(input("Enter your score : "))
#
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("과락")

# score1 = int(input("Enter your score1 : "))
# score2 = int(input("Enter your score2 : "))
# score3 = int(input("Enter your score3 : "))
# avr = ((score1+score2+score3)/3)
# if (score1+score2+score3)/3 >= 90:
#     print("A")
# elif (score1+score2+score3)/3 >= 80:
#     print("B")
# elif (score1+score2+score3)/3 >= 70:
#     print("C")
# elif (score1+score2+score3)/3 >= 60:
#     print("D")
# else:
#     print("F")
#
# print("Your final score is {}".format(round(avr, 3)))


score = int(input("Enter your score : "))
if score >= 60:
    if score == 100:
        print("만점")
    else:
        print("합격")
else:
    if score == 0:
        print("....")
    else:
        print("불합격")