import random
print('')
print('===============HELLO WELCOME TO YOUR===============')
print('======================FUTURE=======================')
print('')
print('please type your name')
print('')
name = input()
print('')
print('ok')
print('now your fortune is...')
print('')
def getAnswer(answerNumber):

    if answerNumber == 1:
           return 'You will DIE DIE DIE'
    elif answerNumber == 2:
           return 'Nooooooooooooooo'
    elif answerNumber == 3:
           return 'You will have the high ground'
    elif answerNumber == 4:
           return 'Take care of yourself first. Then help others.'
    elif answerNumber == 5:
           return 'Ask again later'
    elif answerNumber == 6:
           return 'Your mistake is asking me. Try not to make it again.'
    elif answerNumber == 7:
           return 'You are not a young man anymore'
    elif answerNumber == 8:
           return 'Your outlook is not so good'
    elif answerNumber == 9:
           return 'You want a medal?'
    elif answerNumber == 10:
           return 'GET OFF MY LAWN'
    elif answerNumber == 11:
           return 'Bye have a good time'
    elif answerNumber == 12:
           return 'Im the one who does his job. Im thinking, youre the other one...'


r = random.randint(1, 12)
fortune = getAnswer(r)
print(fortune)
print('')
