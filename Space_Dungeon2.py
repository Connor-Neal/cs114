import time
import sys

print ('')

from random import randrange

text = "=========== HELLO WELCOME TO SPACE DUNGEON =============="

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0.1"
    seconds = float(seconds)
    time.sleep(seconds)

print ('')
print ('')

from random import randrange

text = "To start type in the name of your character"

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0.08"
    seconds = float(seconds)
    time.sleep(seconds)

print ('')
print ('')
Name = input()
print ('')

from random import randrange

text = "Ok now type one of the classes to choose from " + Name

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0.08"
    seconds = float(seconds)
    time.sleep(seconds)


print ('')
print ('')
print ('Mage, Warlock, Warrior, Archer')
print ('')
chr_class = input()

while chr_class != 'Mage' and chr_class != 'Warrior' and chr_class != 'Archer':
    print ('')
    print ('')

    from random import randrange

    text = "Not a real class TRY AGAIN"

    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        seconds = "0.08"
        seconds = float(seconds)
        time.sleep(seconds)

    print ('')
    print ('')
    print ('Mage, Warlock, Warrior, Archer')
    print ('')
    Class = input()

else:
    print ('')
print ('')

from random import randrange

text = "Ok, So these are the stats that you have entered"

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0.08"
    seconds = float(seconds)
    time.sleep(seconds)

print ('')
print ('')
print ('Your Name is:' + Name)
print ('Your class is:' + chr_class)
print ('Your Health points are: 50')
print ('Your Magic points are: 50')
print()
input('Press any key to continue')
print()
print ('....Somewere in a Space Dungeon')
print ('you have entered a battle')

spell = int()
spell = 50
hp = 50
while spell >= 0:
    input()
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

print()

from random import randrange

text = "YOU ARE DEAD"

print ()
print ()

for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    seconds = "0.05"
    seconds = float(seconds)
    time.sleep(seconds)

print ()
print ()
