# def koreaIt(x):
#     return x + "코리아아이티"
# a= koreaIt("인천점 ")
# print(a)
#
# def add(x,y):
#     return x + y
# print(add(1,2))
#
# def wordLength(word):
#     if len(word) >= 5:
#         return "글자가 길다"
#     else:
#         return "글자가 짧다"
#
# word = input("enter a word : ")
# print(word)
# print(wordLength(word))


# def repeat(repeatNum, repeatEmo):
#     return [repeatEmo for i in range(repeatNum)]
#
# repeatNum = int(input("Enter any number : "))
# repeatEmo = input("Enter any emoticon you want to repeat : ")
# print(repeat(repeatNum,repeatEmo))


sportList = ["⚽", "⚾", "🏀", "🏐", "🏈"]

def nextSport(sport):
    dict = {
        "⚽": "⚾"
        , "⚾": "🏀"
        , "🏀": "🏐"
        , "🏐": "🏈"
        , "🏈": "⚽"
    }
    return dict[sport]
