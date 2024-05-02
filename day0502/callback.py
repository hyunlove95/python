def abc(x):
    print("abc")
    x()

def defg():
    print("defg")

abc(defg)

# ==============================

def killing_monster(monster, event):
    print(f"killing {monster}")
    event()

def getGold(n):
    return n
def getFood():
    print("getFood")

print(killing_monster("슬라임", getGold(5)))
print(killing_monster("늑대", getFood))