
spell = int()
spell = 50
hp = 50
while spell >= 0:
    print("")
    print("you cast a spell")
    print("")
    print("you have ", spell, " Magic fuel left")
    spell -= 10
    print("you used 10 Magic fuel")

for attack in range(5):
    print(hp)
    print("you have ", hp , " HP left")
    hp -= 10
