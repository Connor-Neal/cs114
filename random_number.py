import random

def roll():
    print('')
    print('Hello')
    print('')
    print('Roll two dice')
    input()
    r = random.randint(1, 6)
    rr = random.randint(1, 6)
    print('you will move')
    print(r, '+', rr)
    print('spaces forword')
    print('')
    print('landed on the word to number spot')


def randomword(word):
 print('')
 print('type a word')
 print('')
 word = input()
 num = len(word)
 result = random.randint(0, num * 23)
 return result

roll()
result = randomword('python')
print(result)
